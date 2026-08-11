def show_menu():
    print("+" * 30)
    print("🧁 베이킹 이모저모")
    print("=" * 30)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 30)


def get_menu_choice():
    while True:
        menu = input("번호를 입력하세요: ").strip()

        if menu == "":
            print("입력값이 비어 있습니다. 1~5 사이의 번호를 입력하세요.")
            continue

        try:
            choice = int(menu)
        except ValueError:
            print("숫자만 입력할 수 있습니다. 1~5 사이의 번호를 입력하세요.")
            continue

        if choice < 1 or choice > 5:
            print("잘못된 번호입니다. 1~5 사이의 번호를 입력하세요.")
            continue

        return choice


def run_menu():
    while True:
        show_menu()
        menu = get_menu_choice()

        if menu == 1:
            print("퀴즈 풀기")
        elif menu == 2:
            print("퀴즈 추가")
        elif menu == 3:
            print("퀴즈 목록")
        elif menu == 4:
            print("점수 확인")
        elif menu == 5:
            print("프로그램을 종료합니다.")
            break


try:
    run_menu()
except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
