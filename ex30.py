# 해당 부분에서는 사실 finally를 쓰는데 의미가 없음.
from typing import final


try:
    # 예외가 발생할 가능성이 있는 코드
    number = int(input("> 정수 입력"))
    print("입력 값은 {}입니다.".format(number))
except:
    # 예외가 발생했을 경우 실행할 코드
    print("예외가 발생했습니다.")
finally:
    # 무조건적으로 실행하는 코드
    print("무조건적으로 실행됩니다.")
print("무조건 실행됩니다.")
# 11라인과 12라인이 문법적으론 다르지만 실행 결과는 같음.
# 예외 처리에서 어떻게 되든 해당 부분은 같은 방식으로 실행됨.
# 때문에 이러한 일반적인 경우의 finally 구문은 의미가 없음.

# finally를 의미있게 쓰게 되는 경우
# 1. 함수 내부에서 사용할 때 : return
# 2. 반복문 내부에서 사용할 때 : break
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

test()