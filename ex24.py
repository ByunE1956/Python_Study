from ast import Expression
from types import LambdaType


def call_10_times(func):
    for i in range(10):
        # 콜백함수 : 내가 호출하는 것이 아니라 다른 어떤 함수에서 호출하는 것
        func(i)

#def print_hello(number):
#    print("안녕하세요", number)

#call_10_times(print_hello)

# 람다 : 한 줄짜리 함수를 쉽게 정의해서 사용할 수 있게 함
call_10_times(lambda number: print("안녕하세요", number))

# 람다를 응용하는 함수
# 1. filter() 함수
def 짝수만(number):
    return number % 2 == 0

a = list(range(100))
b = filter(짝수만, a)
# 람다를 쓰면
c = filter(lambda number: number % 2 == 0, a)
실험 = lambda number: number % 2 == 0
print(실험)
print(list(c))

# 2. map() 함수 : 기존의 리스트를 기반으로 새로운 리스트를 만들 때 사용
def 제곱(number):
    return number * number

a = list(range(100))
print(list(map(제곱, a)))
# 람다를 쓰면
print(list(map(lambda number: number * number, a)))

# 리스트 내포와 같은 효과를 가진다
print([i * i for i in a if i % 2 == 0]) # <= 리스트 내포는 메모리 용량을 차지한다.

# 메모리를 절약하고 싶을 때는 map(), filter()함수를 사용
# 메모리 상관없이 간단한 코드 작성이면 그냥 리스트 내포를 사용해도 무방
# But, 현대 컴퓨터는 사양이 좋아서 리스트 내포를 사용해도 크게 차이 없음.
# 최근에는 리스트 내포를 더 많이 사용하는 추세이다.