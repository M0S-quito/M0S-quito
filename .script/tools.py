from pathlib import Path
import shutil
import sys

TEMPLATE_MAP = {
    "public_task": ["99_Templates/PublicTask.md", "00_Data/01_PublicTasks"],
    "private_task": ["99_Templates/PrivateTask.md","00_Data/02_PrivateTasks"],
    "routine": ["99_Templates/Routine.md", "00_Data/03_Routines"],
    "bin": ["99_Templates/Bin.md", "00_Data/04_Bins"]
}
BASE_DIR = Path("./") # 현재 디렉토리를 기준으로 경로 설정(짜피 샤뱅으로 할꺼임)

# Template로 Task만들기
def template(template_name: str, filename: str):
    if template_name not in TEMPLATE_MAP:
        raise ValueError(f"Template '{template_name}' not found.")

    template_path = BASE_DIR / TEMPLATE_MAP[template_name][0]
    target_dir = BASE_DIR / TEMPLATE_MAP[template_name][1]

    target_dir.mkdir(parents=True, exist_ok=True)

    new_file = target_dir / f"{filename}.md"

    shutil.copy(template_path, new_file)

    print(f"Created: {new_file}")

# 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools.py <template> <filename>")
        sys.exit(1)

    template(sys.argv[1], sys.argv[2])
