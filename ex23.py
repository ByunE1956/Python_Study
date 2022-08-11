# <튜플>
# 튜플이 리스트와 다른 기본적인 부분
# 1. 대괄호가 아니라 소괄호로 선언
# 2. 한 번 선언하면 값을 바꿀수 없음

from http.client import OK


a = (1, 2, 3, 4)
print(a[0])

# 튜플을 사용하는 경우(1) : 복합할당
[a, b] = [10, 20]
(c, d) = (30, 40)
print(a, b, c, d)

# 괄호가 없어도 튜플로 인식될 수 있다면 튜플
c, d = 30, 40
print(c, d)

# 대표적으로 사용하는 경우(2) : 스왑
a, b = 10, 20
print(a, b)
a, b = b, a # 스왑(튜플을 사용하면 별도의 변수 없이 바로 스왑 가능)
print(a, b)

# 튜플을 사용하는 경우(3) : 튜플을 리턴하는 함수
a, b = 97, 40
print(divmod(a, b))

# 이전에 사용했던 for문에서의 튜플
for i, value in enumerate([1, 2, 3, 4, 5, 6]):
    print("{}번째 요소는 {}입니다.".format(i, value))

# 함수에서의 튜플 return
def tuple():
    return 10, 20
a, b = tuple()
print(a, b)

# 튜플에서 자주 실수하는 부분
print([273])
print(type([273]))
# 괄호로 튜플처럼 만들어도 해당 부분은 그저 int
print((273))
print(type((273)))
# 요소가 하나인 경우에 tuple을 만들고 싶다면 쉼표를 추가해야한다
print((273, ))
print(type((273, )))

# dictionary에서 list는 key가 될 수 없지만 tuple은 키가 될 수 있다
#a = {
#    숫자:    OK
#    문자열:  OK
#    불:      OK
#    리스트:  XXX
#    튜플:    OK
#}

a = {
    (0, 0): 10,
    (0, 1): 20,
    (0, 2): 30,
    (0, 3): 40
}
print(a[(0, 0)])
print(a[0, 0])