---
priority: medium
status: in_progress
tags: [M0S_Task]
deadline: 2026-03-07 23:00
start_date: 2026-02-22
end_date:
deploy: false
---
### SubTask
- [ ] CLI 기본 구조 만들기(core.py및main.py)
- [ ] 설정 파일 설계 (config.json)
- [ ] md 파싱 모듈 작성
- [ ] 경로 유틸 모듈 작성
---
# Main

# 📌 2026-03-02 개발 작업 전체 정리

## 1. CLI 구조 설계 및 구현

### 목표
- 파일 기반 Task 시스템을 CLI 명령어 형태로 조작 가능하도록 설계
- create / log 기능을 명령어로 분리
- 엔진(core)과 인터페이스(main) 분리

### 구현 내용

#### 1-1. main.py (CLI 엔트리)

- argparse 기반 CLI 구조 생성
- subcommand 구조 채택
- create / log 명령 분리

구현된 명령:

```

task create <type> <name>
task log

```

#### 역할 분리 구조

- main.py → 입력 해석기
- core.py → 실제 로직 실행

이로써 CLI 레이어와 엔진 레이어 분리 완료.

---

## 2. Template 기반 파일 생성 시스템

### 목표
- 템플릿 파일을 기반으로 지정 폴더에 자동 생성
- 파일 생성 시 frontmatter 중복 문제 해결
- 확장 가능한 매핑 구조 설계

### TEMPLATE_MAP 구조 설계

```python
TEMPLATE_MAP = {
    "public_task": ["99_Templates/PublicTask.md", "01_PublicTasks"],
    "private_task": ["99_Templates/PrivateTask.md","02_PrivateTasks"],
    "routine": ["99_Templates/Routine.md", "03_Routines"],
    "bin": ["99_Templates/Bin.md", "04_Bins"],
    "log": ["99_Templates/Log.md", "00_Logs"]
}
````

### 구현 완료 사항

* BASE_DIR 기반 상대경로 처리
* 대상 폴더 자동 생성 (mkdir parents=True)
* 파일 존재 시 덮어쓰기 방지 로직 추가
* template() 함수가 파일 경로 반환하도록 개선

---

## 3. Frontmatter 파서 구현

### 목표

* Markdown 파일을 데이터베이스처럼 활용
* frontmatter를 dict 형태로 파싱

### 구현 내용

* `---` 기준으로 frontmatter 영역 인식
* key: value 형식 분리
* dict로 반환

이로써 md 파일이 데이터 객체 역할 수행 가능.

---

## 4. 완료 Task 집계 로직 구현

### 목표

* 오늘 완료된 Task만 자동 수집
* status + end_date 기준 필터링

### 로직 설계

완료 조건:

```
status == "done"
AND
end_date == 오늘 날짜
```

### 순회 대상

* 01_PublicTasks
* 02_PrivateTasks

### 결과

* 파일명(stem)만 추출하여 리스트 반환
* Log 자동 삽입용 데이터 확보

---

## 5. Routine 자동 집계 로직 구현

### 목표

* 03_Routines 폴더 내 모든 루틴 파일 자동 수집

### 구현 방식

* glob("*.md") 기반 파일 순회
* 파일명(stem) 추출

---

## 6. Log 자동 갱신 시스템 설계

### 기존 문제

* 단순 템플릿 복사 방식은 일기 영역 덮어쓰기 위험 존재
* Log는 자동 영역 + 수동 영역 공존 문서

### 현재 Log 구조

```
---
date:
feeling:
sleep:
focus:
day_score:
---

### 🔁Routines

---

### ✅Tasks complated

---

### 🧠Review
```

### 해결 방식

* 섹션 제목 기준 블록 교체 방식 채택
* Routines / Tasks 영역만 자동 갱신
* frontmatter 및 Review 영역은 유지

### 구현된 처리 흐름

1. Log 파일 없으면 template("log", today)
2. 파일 읽기
3. Routines 섹션 내용 교체
4. Tasks 섹션 내용 교체
5. 파일 재작성

---

## 7. 전체 디렉토리 설계 확정

```
.script/
 ├─ main.py          ← CLI 엔트리
 ├─ core.py          ← 메인 엔진
 ├─ config.json      ← (예정)
```

### 역할 정리

* main.py → 사용자 인터페이스
* core.py → 로직 처리
* md 파일 → 데이터베이스
* Log → 집계 + 일기 복합 문서

---

## 8. 오늘 작업 결과 요약

### 완료된 SubTask

* [x] CLI 기본 구조 만들기 (core.py 및 main.py)
* [x] md 파서 모듈 작성
* [x] 경로 유틸 구조 설계 (BASE_DIR 기반 분리)
* [x] Log 자동 집계 시스템 구현
* [x] 완료 Task 필터링 로직 구현

### 진행 중

* [ ] config.json 설계
* [ ] task done 명령 추가
* [ ] streak/통계 시스템 설계

---

## 9. 현재 시스템 상태

* 파일 기반 Task 엔진 구조 확정
* Markdown을 DB처럼 활용 가능
* Log는 집계 + 일기 공존 구조로 안정화
* CLI 확장 가능 구조 완성

현재 단계는:

> 뼈대 완성 → 기능 확장 단계 진입 직전

---

## 10. 다음 단계 계획

1. task done <파일명> 명령 구현

   * status 자동 변경
   * end_date 자동 삽입
   * log 자동 업데이트

2. config.json 설계

   * 기본 폴더 경로 설정
   * 날짜 포맷 설정
   * 향후 확장 대비

3. 통계 기능 설계

   * 완료 streak
   * 일일 생산성 점수 연동
   * 감정/수면 데이터 분석 기반 확장 가능성 확보

---

# 결론

오늘 작업은 단순 기능 추가가 아니라
시스템 아키텍처를 확정한 날이다.

이제 M0S_Task는:

* 파일 기반 개인 운영 시스템
* Markdown을 DB로 사용하는 엔진
* CLI 확장형 구조

로 진입했다.

```

---

이 정도면 오늘 작업 전부 기록 완료다.  
이제 이 프로젝트는 그냥 Todo가 아니라  
점점 “개인 OS 코어”가 되어가고 있다.
```
