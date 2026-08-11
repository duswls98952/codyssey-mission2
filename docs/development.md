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
![GitHub 원격 저장소 push](screenshots/git-push.png)

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

