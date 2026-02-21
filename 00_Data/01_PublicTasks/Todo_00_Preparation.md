---
priority: medium
status: in_progress
tags: M0S_Task
deadline: 2026-02-22 20:00
start_date: 2026-02-21
end_date:
deploy: false
---
### SubTask
- [ ] 

---
# Main
### 시작한 이유
나에게 맞는 Todo리스트를 만들고 싶었다. 
사실 손수 todo를 하나한 작성해도 되겠지만 군대에서 작업을 하다 보니 절대적인 시간도 부족하고 
작성하는 시간만 길어져 가니 점점 지쳐가게 되어서 어느정도 자동화 해야겠다는 생각을 하게 되었다.
> 솔직히 기성 앱이나 웹들도 있는데 뭔가 하나씩 맘에 안드는 부분이나 나에게 필요 없는 부분들이 보여서 또 직접 만드는 맛도 있으니 만들어 보기로 했다...

그래서 나의 모든 작업 내용이 들어갈 레포이니 나를 설명하는 `Profile Repository`에 작성하기로 하였다.
추후에 각종 프로젝트나 다른 레포에 대한 설명 같은것도 들어갈꺼 같으니 그 시작점인 `Profile Repository`레포가 제격이라 생각했다.
내게 가장 친숙한 노트앱인 `Obsidian`을 기반해 작성할 것이며 자동화는 일단 termux/tasker기반을 생각하고 있다.

### 디렉토리 구조
```
.obsidian/
.script/
00_Data/
    01_PublicTasks/
    02_PrivateTask/
    03_Routines/
    04_Bin/
01_Logs/
99_Templates/
README.md
Todo.base
```
- `.obsidian/` : 옵시디언 플러그인 및 설정 파일
- `.script/` : 각종 자동화 스크립트가 들어갈 파일
- `00_Data/` : 내 할일들이나 임시 노트가 들어갈 파일
    - `01_PublicTasks/` : 외부에 공개 되어도 되는 TODO 폴더
    - `02_PrivateTask/` : 외부에 공개되면 안되는 사적인 TODO 폴더
    - `03_Routines/` : 반복적으로 해야 하는 작업들이 들어갈 폴더
    - `04_Bin/` : 내 잡다한 생각이 들어갈 작은 임시 노트 폴더
- `01_Logs/` : 매일 어떤 작업을 했는지 하루를 평가하는 Log가 들어가는 폴더
- `99_Templates/` : 각종 템플릿이 들어갈 폴더
- README.md : 내가 하고 있는 작업이나 현재 상황 나에대한 설명이 매일 업로드 되어 profile에 보여질 파일
- Todo.base : 옵시디언에서 파일 필터링을 위해 존하는 옵시디언 전용 파일

### 계획(큰 틀)
- [ ] 📦 Phase 1 – [[Todo_01_CoreEngine.md]]
- [ ] 📦 Phase 2 – [[Todo_02_FileGenerator.md]]
- [ ] 📦 Phase 3 – [[Todo_03_TaskEngine.md]]
- [ ] 📦 Phase 4 – [[Todo_04_RoutineEngine.md]]
- [ ] 📦 Phase 5 – [[Todo_05_OutputLayer.md]]
> 일단 이런 식으로 큰 틀을 나누어 보았다... 
> 세부적인건 각 단계에서 SubTask로 잡아가보자


### 시작전 마음가짐
일단 Todo를 만들고 있다고 작업이 안될 이유는 없다. 자동화가 없어도 내 손으로 쓰면 된다.
오래 쓸 목적으로 만드는 것이니 최대한 공들여 만들어 보고자 한다. 
이게 군대에서의 마지막 프로젝트가 될 것 같다. 훈련이 좀 있긴 하지만 최대한 군대 안에서 완성 하고 싶다!