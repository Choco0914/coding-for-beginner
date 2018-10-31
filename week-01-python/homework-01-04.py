# 에러 나지 않는 구구단
# 구현 내용
"""
사용자가 어떤 값을 넣더라도 에러가 나지 않도록 처리해 봅시다.
- (추가 과제에서 2~9라는 숫자 외에는 구구단이 출력하지 않도록 출력했습니다.)
- 예를 들어 , 혀냊 숫자가 아닌 "1단" 이라는 문자를 넣으면
구구단이 실행되지 않고 종료됩니다.
- 잘못된 값을 입력한 경우, "2에서 9사이의 숫자만 입력해주세요." 이라는
문구와 함께 다시 구구단이 실행되도록 합시다.
"""
def gugudan():
    try:
        dan = int(input("2에서 9사이의 숫자를 입력해주세요: "))
        if dan > 1 and dan < 9:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan()
    except:
        print("알 수 없는 에러가 발생 했습니다.")
        gugudan()

gugudan()
