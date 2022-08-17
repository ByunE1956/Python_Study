# 구문 오류 : 코드 자체에 문제가 있어서 실행 불가
# 예외(런타임 오류) : 코드 자체는 문제가 없으나 실행과 관련된 문제가 있는것 실행은 가능 하나 원하는 결과 도출 불가(실행 도중 죽음 등)

# 숫자를 입력받습니다.
#number_input_a = int(input("정수 입력> "))  # 정수를 제외한 다른 타입을 입력하면 예외 출력

# 기본예외처리
while True:
    string_input = input("정수 입력> ")
    if string_input.isdigit():
        number_input_a = int(string_input)
        # 출력합니다.
        print("원의 반지름:", number_input_a)
        print("원의 둘레:", 2 * 3.14 * number_input_a)
        print("원의 넓이:", 3.14 * number_input_a ** 2)
        break
    else:
        print("정수를 입력하세요!")
