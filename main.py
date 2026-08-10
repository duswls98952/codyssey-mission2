while True:
    print("+" * 30)
    print("🧁 베이킹 이모저모")
    print("=" * 30 )
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 30)

    menu = input("번호를 입력하세요: ")

    if menu == "1":
        print("퀴즈 풀기")
    elif menu == "2":
        print("퀴즈 추가")
    elif menu == "3":
        print("퀴즈 목록")
    elif menu == "4":
        print("점수 확인")
    elif menu == "5":
        print("프로그램을 종료합니다.")
        break

