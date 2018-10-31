# 맛집 고르기
# 1)구현 내용
"""
처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식중 한가지를 고르라는 내용이 나옵니다.
그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해줍니다.
"""
import random
# 추천해줄 리스트를 만들어준다.
KOREAN_FOOD = ("삼겹살", "냉면", "짜그리")
CHINESE_FOOD = ("짜장면", "탕수육", "짬뽕")
JAPANESE_FOOD = ("라멘", "돈까스", "돈카츠")
choice_result = ""
# 사용자로부터 입력을 받는다.
food_user = input("한식, 중식 일식 중 한가지를 골라보세요!")

# 임의로 추천해준다.
if food_user == "한식":
    choice_result = random.choice(KOREAN_FOOD)
elif food_user == "중식":
    choice_result = random.choice(CHINESE_FOOD)
elif food_user == "일식":
    choice_result == random.choice(JAPANESE_FOOD)
else:
    print("한식, 일식, 중식 중에서 선택해주세요!")

if choice_result:
    print("{} 중에서 {}가 선택되었습니다.".format(food_user, choice_result))
