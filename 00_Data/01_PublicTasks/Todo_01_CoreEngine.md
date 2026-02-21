---
priority:
status: 
tags:
deadline:
start_date: 
end_date:
deploy: false
---
### SubTask
- [ ] CLI 기본 구조 만들기
- [ ] 설정 파일 설계 (config.json)
- [ ] md 파서 모듈 작성
- [ ] 경로 유틸 모듈 작성
---
# Main
### 1. 템플릿 파일 기반으로 바로 해당 폴더에 파일 생성시 알맞는 템플릿 적용해서 생성하는 스크립트 작성
```python
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
```
#### 제작 이유
왜인지 모르겠는데 base에서 파일을 생성하면 자동으로 원하지 않는 프론트메터가 붙어서 나옴 이러면 내가 템플릿을 적용해도 위에 덮어져서 중복이 되버림;;
#### 제작 방식
- 일단 폰(termux)에서 만이 아니라 컴에서도 사용할 수도 있어서 로직은 python으로 작성
- termux에서 .sh파일로 감싼다음에 Tasker에서 호출해서 사용할 예정
