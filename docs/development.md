# Development Log

## 1. 초기 개발 환경 및 Git 저장소 설정

관련 요구사항:
- 4-1. Git 저장소 설정
- 7. 제출물: 개발 환경 설정 스크린샷

작업 내용:
- Python 및 Git 버전 확인
- Git 저장소 초기화
- .gitignore, README.md, main.py 생성
- 초기 커밋 생성
- GitHub 원격 저장소 push
- pull 상태 확인

증빙 자료:

### Python 및 Git 버전 확인
![Python 및 Git 버전 확인](screenshots/Python_Git버전확인.png)

### Git 저장소 초기화
![Git 저장소 초기화](<screenshots/git init_status.png>)

### 기본 파일 생성
![기본 파일 생성](<screenshots/gitignore_README파일 생성.png>)

### 변경 파일 스테이징 및 상태 확인
![변경 파일 스테이징 및 상태 확인](screenshots/git_add_git_status.png)

### 초기 커밋 생성
![초기 커밋 생성](screenshots/git_commit_Initial_project_setup_.png)

### GitHub 원격 저장소 push
![GitHub 원격 저장소 push](screenshots/git_push.png)

### pull 상태 확인
![pull 상태 확인](screenshots/git_status_git_pull_Already_up_to_date.png)

## 2. 메뉴 기능 구현

관련 요구사항:
- 4-2. 메뉴 기능
- 4-3. 공통 입력 / 예외 처리 기준 일부

작업 내용:
- 메뉴 출력 로직을 `show_menu()` 함수로 분리
- 메뉴 입력 처리 로직을 `get_menu_choice()` 함수로 분리
- 입력 앞뒤 공백 제거 처리
- 빈 입력, 숫자가 아닌 입력, 허용 범위 밖 숫자 입력 처리
- `KeyboardInterrupt`, `EOFError` 발생 시 안내 메시지 출력 후 안전 종료 처리

검증 내용:
- 빈 입력, 문자 입력, 범위 밖 숫자 입력 후 다시 입력받는 흐름 확인
- `5` 입력 시 프로그램 종료 확인

## 3. Quiz 클래스 구현

관련 요구사항:
- 4-4. Quiz 클래스

작업 내용:
- 개별 퀴즈를 표현하는 `Quiz` 클래스 추가
- 문제 문장, 보기 목록, 정답 번호를 속성으로 저장
- 문제와 보기를 출력하는 `display()` 메서드 추가
- 사용자의 답과 정답을 비교하는 `is_correct()` 메서드 추가

검증 내용:
- `Quiz` 객체 생성 후 문제와 보기 출력 확인
- 정답 번호 비교 결과 확인

## 4. 기본 퀴즈 데이터 작성

관련 요구사항:
- 4-5. 기본 퀴즈 데이터

작업 내용:
- 베이킹 주제의 기본 퀴즈 5개 작성
- 각 퀴즈에 문제, 보기 4개, 정답 번호 포함
- `Quiz` 클래스 인스턴스로 기본 퀴즈 데이터 생성

검증 내용:
- 기본 퀴즈가 5개인지 확인
- 각 퀴즈의 보기가 4개인지 확인
- 각 퀴즈의 정답 번호가 1~4 사이인지 확인

