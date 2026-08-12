class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


default_quizzes = [
    Quiz(
        "파운드 케이크 이름의 유래는?",
        [
            "완성된 케이크가 항상 1파운드라서",
            "밀가루, 버터, 설탕, 달걀을 각각 1파운드씩 넣어서",
            "영국 화폐 파운드에서 이름을 따와서",
            "파운드라는 제빵사가 만들어서",
        ],
        2,
    ),
    Quiz(
        "머랭의 주재료는?",
        [
            "밀가루와 버터",
            "우유와 생크림",
            "달걀흰자와 설탕",
            "초콜릿과 코코아가루",
        ],
        3,
    ),
    Quiz(
        "베이킹소다와 베이킹파우더의 공통 역할은?",
        [
            "반죽을 부풀게 하는 것",
            "반죽의 색을 진하게 만드는 것",
            "반죽을 얼리는 것",
            "단맛을 내는 것",
        ],
        1,
    ),
    Quiz(
        "휘낭시에라는 이름의 뜻과 관련 있는 것은?",
        [
            "프랑스의 꽃 이름",
            "작은 오븐이라는 뜻",
            "금융가 또는 금괴 모양",
            "버터를 태우는 도구 이름",
        ],
        3,
    ),
    Quiz(
        "슈크림의 '슈(chou)'는 프랑스어로 무슨 뜻일까?",
        [
            "구름",
            "크림",
            "작은 빵",
            "양배추",
        ],
        4,
    ),
]


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


def get_required_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("빈 입력은 사용할 수 없습니다.")
            continue

        return text


def get_answer_choice():
    while True:
        answer = input("정답 번호를 입력하세요: ").strip()

        if answer == "":
            print("입력값이 비어 있습니다. 1~4 사이의 번호를 입력하세요.")
            continue

        try:
            choice = int(answer)
        except ValueError:
            print("숫자만 입력할 수 있습니다. 1~4 사이의 번호를 입력하세요.")
            continue

        if choice < 1 or choice > 4:
            print("잘못된 번호입니다. 1~4 사이의 번호를 입력하세요.")
            continue

        return choice


def play_quiz(quizzes):
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return

    score = 0

    for quiz in quizzes:
        print()
        quiz.display()
        user_answer = get_answer_choice()

        if quiz.is_correct(user_answer):
            print("정답입니다!")
            score += 1
        else:
            print("오답입니다.")

    print()
    print(f"총 {len(quizzes)}문제 중 {score}문제를 맞혔습니다.")


class QuizGame:
    def __init__(self):
        self.quizzes = default_quizzes.copy()
        self.best_score = 0

    def add_quiz(self):
        question = get_required_text("문제를 입력하세요: ")

        choices = []
        for number in range(1, 5):
            choice = get_required_text(f"보기 {number} 입력: ")
            choices.append(choice)

        answer = get_answer_choice()
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n등록된 퀴즈 목록")
        print("-" * 30)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def run(self):
        while True:
            show_menu()
            menu = get_menu_choice()

            if menu == 1:
                play_quiz(self.quizzes)
            elif menu == 2:
                self.add_quiz()
            elif menu == 3:
                self.list_quizzes()
            elif menu == 4:
                print("점수 확인")
            elif menu == 5:
                print("프로그램을 종료합니다.")
                break


try:
    game = QuizGame()
    game.run()
except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")
