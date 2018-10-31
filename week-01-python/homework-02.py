# 과제2 회사 조직도 만들기
# 구현 내용
"""
사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이 성별이 존재합니다.
직장 동료 클래스를 사람 클래스를 이용해서 만듭니다. 사람 기본 요소 외 별도의 추가
사항은 직급입니다.
"""

class People:
    """사람 클래스를 정의해준다"""
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Colleague(People):
    """직장 동료 클래스를 정의해준다."""
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

colleage = Colleague("Choco", 20, "Male", "대리")
# print(colleage.name)
print(colleage.__dict__)
