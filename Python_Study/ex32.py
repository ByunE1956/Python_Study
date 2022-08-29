# 학생 리스트를 선언합니다.
#students =[
#    {"name":"윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
#    {"name":"연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
#    {"name":"구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
#    {"name":"나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
#    {"name":"윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
#    {"name":"윤명월", "korean": 64, "math": 88, "english": 92, "science": 92}
#]

# dictionary 를 생성하는 함수
def 학생_생성(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }
# 해당 함수를 사용해서 dictionary 생성
students =[
    학생_생성("윤인성", 87, 98, 88, 95),
    학생_생성("연하진", 92, 98, 96, 98),
    학생_생성("구지연", 76, 96, 94, 90),
    학생_생성("나선주", 98, 92, 96, 92),
    학생_생성("윤아린", 95, 98, 98, 98),
    학생_생성("윤명월", 64, 88, 92, 92)
]


# 학생을 한 명씩 반복합니다.
#print("이름", "총점", "평균", sep = "\t")
#for student in students:
#    # 점수의 총합과 평균을 구합니다.
#    score_sum = student["korean"] + student["math"] +\
#                student["english"] + student["science"]
#    score_average = score_sum / 4
#    # 출력합니다.
#    print(student["name"], score_sum, score_average, sep = "\t")

# 위의 로직을 함수로 구현
def 총점(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]
def 평균(student):
    return 총점(student) / 4
def 출력(student):
    print(student["name"], 총점(student), 평균(student), sep = "\t")

for student in students:
    출력(student)


# 위의 내용을 class 로 작성
class 학생:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def 총점(self):
        return self.korean + self.math + self.english + self.science
    def 평균(self):
        return self.총점() / 4
    def 출력(self):
        print(self.name, self.총점(), self.평균(), sep="\t")

students =[
    학생("윤인성", 87, 98, 88, 95),
    학생("연하진", 92, 98, 96, 98),
    학생("구지연", 76, 96, 94, 90),
    학생("나선주", 98, 92, 96, 92),
    학생("윤아린", 95, 98, 98, 98),
    학생("윤명월", 64, 88, 92, 92)
]
print("# class로 출력")
print("이름", "총점", "평균", sep="\t")
for student in students:
    student.출력()

# 절차지형 프로그래밍 언어
# 동사 + 목적어 : 명령어
#  - 출력(학생)
#  - 평균(학생)
#  - 총합(학생)

# 객체지향 프로그래밍 언어
# 주어 + 동사 + 목적어 : 주어가 행위를 한다
#  - 학생.출력(이름)
#  - 학생.평균(총합)
#  - 학생.총합(과목별 점수)