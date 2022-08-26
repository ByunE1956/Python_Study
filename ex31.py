try:
    number =- int(input("정수 입력> "))
    print("원의 반지름:", number)
    print("원의 둘레:", 2 * 3.14 * number)
    print("원의 넓이:", 3.14 * number ** 2)
except Exception as exception:
    if type(exception) == ValueError:
        print("값에 문제가 있습니다.")


try:
    a = [273, 103, 53, 57, 100]
    number = int(input("정수 입력(0~4까지 입력해주세요)> "))
    print(a[number])

#except Exception as exception:
#    if type(exception) == ValueError:
#        print("값에 문제가 있습니다.")
#    elif type(exception) == IndexError:
#        print("0~4까지 입력해주세요.")

# 들여쓰기를 줄이기 위한 파이썬의 예외처리 방법
except ValueError as exception:
    print("값에 문제가 있습니다.")
except IndexError as exception:
    print("0~4까지 입력해주세요.")
except Exception as exception:  # 해당 부분은 모든 예외의 부모로 위의 예외를 제외한 예외 처리가 해달 부분에서 모두 걸러짐.
    print("알 수 없는 예외가 발생했습니다.")

# raise 예외객체
# 개발자가 실수를 할 때 프로그램을 강제로 종료시키기 위한 예외
# 개발자들은 잘 안쓰고 개발자들이 사용하는 라이브러리를 개발할 때 사용.
raise Exception("안녕하세요")