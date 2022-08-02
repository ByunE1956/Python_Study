# break Practice
i = 0

while True:
    print("{}번째 반복중입니다.".format(i))
    i += 1

    input_text = input("> 종료하시겠습니까?(y/n)")
    if input_text in ["Y", "y"]:
        print("While문을 종료합니다")
        break

# continue Practice
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue
    # Python 같은 경우는 들여쓰기의 특성상 continue를 사용하게되면 들여쓰기 단계를 줄일 수 있다.
    print(number)
