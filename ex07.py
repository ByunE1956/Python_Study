#x = int(input("> 정수를 입력하세요: "))
#
#if 10 < x < 20:
#    print("조건에 맞습니다")

str_input = input("태어난 해를 입력해주세요> ")
birth_year = int(str_input) % 12

if birth_year == 0:
    print("원숭이 띠입니다.")
elif birth_year == 1:
    print("닭 띠입니다.")
elif birth_year == 2:
    print("개 띠입니다.")
elif birth_year == 3:
    print("돼지 띠입니다.")
elif birth_year == 4:
    print("쥐 띠입니다.")
elif birth_year == 5:
    print("소 띠입니다.")
elif birth_year == 6:
    print("범 띠입니다.")
elif birth_year == 7:
    print("토끼 띠입니다.")
elif birth_year == 8:
    print("용 띠입니다.")
elif birth_year == 9:
    print("뱀 띠입니다.")
elif birth_year == 10:
    print("말 띠입니다.")
else:
    print("양 띠입니다.")