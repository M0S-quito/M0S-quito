from pathlib import Path
import shutil
import sys
from datetime import datetime

TEMPLATE_MAP = {
    "public_task": ["99_Templates/PublicTask.md", "01_PublicTasks"],
    "private_task": ["99_Templates/PrivateTask.md","02_PrivateTasks"],
    "routine": ["99_Templates/Routine.md", "03_Routines"],
    "bin": ["99_Templates/Bin.md", "04_Bins"],
    "log": ["99_Templates/Log.md", "00_Logs"]
}

BASE_DIR = Path("./")


# ------------------------
# TEMPLATE 생성
# ------------------------
def template(template_name: str, filename: str):
    if template_name not in TEMPLATE_MAP:
        raise ValueError(f"Template '{template_name}' not found.")

    template_path = BASE_DIR / TEMPLATE_MAP[template_name][0]
    target_dir = BASE_DIR / TEMPLATE_MAP[template_name][1]

    target_dir.mkdir(parents=True, exist_ok=True)

    new_file = target_dir / f"{filename}.md"

    if not new_file.exists():
        shutil.copy(template_path, new_file)
        print(f"Created: {new_file}")

    return new_file


# ------------------------
# FRONTMATTER 파싱
# ------------------------
def frontmatter_parsing(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != "---":
        return {}

    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()

    return data


# ------------------------
# DONE TASK 필터
# ------------------------
def get_done_tasks_by_date(date_str: str):
    result = []
    task_dirs = ["01_PublicTasks", "02_PrivateTasks"]

    for folder in task_dirs:
        dir_path = BASE_DIR / folder
        if not dir_path.exists():
            continue

        for file in dir_path.glob("*.md"):
            meta = frontmatter_parsing(file)

            if meta.get("status") == "done" and meta.get("end_date") == date_str:
                result.append(file.stem)

    return result


# ------------------------
# ROUTINE 목록
# ------------------------
def get_routines():
    routine_dir = BASE_DIR / "03_Routines"
    if not routine_dir.exists():
        return []

    return [f.stem for f in routine_dir.glob("*.md")]


# # ------------------------
# # AUTO 구간 교체 함수
# # ------------------------
# def replace_section(content, start_marker, end_marker, new_block):
#     start = content.find(start_marker)
#     end = content.find(end_marker)

#     if start == -1 or end == -1:
#         return content  # 마커 없으면 건드리지 않음

#     start += len(start_marker)

#     return (
#         content[:start]
#         + "\n"
#         + new_block
#         + "\n"
#         + content[end:]
#     )


# # ------------------------
# # LOG 업데이트
# # ------------------------
# def update_log():
#     today = datetime.now().strftime("%Y-%m-%d")

#     log_file = template("log", today)

#     with open(log_file, "r", encoding="utf-8") as f:
#         content = f.read()

#     routines = get_routines()
#     done_tasks = get_done_tasks_by_date(today)

#     routine_block = "\n".join([f"- [ ] {r}" for r in routines])
#     done_block = "\n".join([f"- [x] {d}" for d in done_tasks])

#     content = replace_section(
#         content,
#         "## AUTO_ROUTINE_START",
#         "## AUTO_ROUTINE_END",
#         routine_block
#     )

#     content = replace_section(
#         content,
#         "## AUTO_DONE_START",
#         "## AUTO_DONE_END",
#         done_block
#     )

#     with open(log_file, "w", encoding="utf-8") as f:
#         f.write(content)

#     print(f"Updated log: {log_file}")




def replace_between_sections(content, section_title):
    lines = content.splitlines()
    new_lines = []
    inside_section = False

    for i, line in enumerate(lines):
        if line.strip() == section_title:
            new_lines.append(line)
            new_lines.append("")  # 내용 비우고 시작
            inside_section = True
            continue

        if inside_section and line.strip() == "---":
            new_lines.append("---")
            inside_section = False
            continue

        if not inside_section:
            new_lines.append(line)

    return "\n".join(new_lines)


def update_log():
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = template("log", today)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    routines = get_routines()
    done_tasks = get_done_tasks_by_date(today)

    routine_block = "\n".join([f"- [ ] {r}" for r in routines])
    done_block = "\n".join([f"- [x] {d}" for d in done_tasks])

    # Routines 섹션 교체
    content = inject_section(
        content,
        "### 🔁Routines",
        routine_block
    )

    # Tasks 섹션 교체
    content = inject_section(
        content,
        "### ✅Tasks complated",
        done_block
    )

    with open(log_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated log: {log_file}")


def inject_section(content, title, new_block):
    parts = content.split(title)

    if len(parts) < 2:
        return content  # 섹션 없으면 건드리지 않음

    before = parts[0]
    rest = parts[1]

    # 다음 --- 기준으로 나누기
    section_parts = rest.split("---", 1)

    if len(section_parts) < 2:
        return content

    after = section_parts[1]

    rebuilt = (
        before
        + title
        + "\n"
        + new_block
        + "\n---"
        + after
    )

    return rebuilt


# ------------------------
# CLI 진입점
# ------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tools.py template <type> <filename>")
        print("  python tools.py log")
        sys.exit(1)

    command = sys.argv[1]

    if command == "template":
        if len(sys.argv) < 4:
            print("Usage: python tools.py template <type> <filename>")
            sys.exit(1)
        template(sys.argv[2], sys.argv[3])

    elif command == "log":
        update_log()