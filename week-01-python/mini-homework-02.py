# School class

class MiddleSchool:
    """중학교 class를 정의해준다"""
    def __init__(self, name, build_year, adress):
        self.name = name
        self.build_year = build_year
        self.adress = adress

middle = MiddleSchool("갈뫼중학교", "2002", "경기도 의왕시 갈미로 61")
print(middle.name)
print(middle.build_year)
print(middle.adress)
