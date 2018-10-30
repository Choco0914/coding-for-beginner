# 가위 바위 보 게임
# 구현 내용
"""
사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
"""
import random

ROCK = "바위"
SCISSORS = "가위"
PAPER = "보"
computer_rps =(
    ROCK,
    SCISSORS,
    PAPER
)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count < 3:
    """가위바위보 승부가 날때까지 반복한다."""
    user_choice = input("가위, 바위, 보 중 하나를 고르세요!")
    computer_choice = random.choice(computer_rps)
    if user_choice == computer_choice:
        print("비겼습니다.")
    elif ((user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS
            and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)):
        win_count = win_count + 1
        print("이겼습니다.")
    elif ((computer_choice == ROCK and user_choice == SCISSORS)
        or (computer_choice == SCISSORS
            and user_choice == PAPER)
        or (computer_choice == PAPER and user_choice == ROCK)):
        lose_count = lose_count + 1
        print("졌습니다.")
    else:
        print("가위, 바위 그리고 보 세가지 중 고르세요!")

if win_count == 3:
    print("사용자가 최종 승리 하였습니다.")
else:
    print("컴퓨터가 최종 승리 하였습니다 ㅎㅎ")
