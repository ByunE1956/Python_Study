number1 = int(input("> 1번째 숫자: "))
number2 = int(input("> 2번째 숫자: "))
print()

if number1 > number2:
    print("처음 입력했던 {}가 {}보다 더 큽니다.".format(number1, number2))
if number1 < number2:
    print("두 번째로 입력했던 {}가 {}보다 더 큽니다.".format(number2, number1))