# exceptions (bug)

# ZeroDivisionError
# 1 / 0

def divide_by(first, second):
    """second으로 first를 나눠준다"""
    try:
        return first / second
    except:
        return "0으로 나눌 수 없습니다."

print(int(divide_by(4, 2)))
print(divide_by(4, 0))

# 예외 만들기
# exception
class EvenNumberDevisionError(Exception):
    pass

def divide_by_odd_number(first, second):
    """홀수만 표시해준다"""
    if second % 2 == 0:
        raise EvenNumberDevisionError
    else:
        return first / second

print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))
