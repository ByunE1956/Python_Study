# 제너레이터
"""
간단하게 "이터레이터를 직접 만들 때 사용하는 구문"
함수 내부에 yield 라는 키워드가 포함되면 해당 함수는 제너레이터가 된다.
"""
# next함수 한번 호출시 yield까지 실행되고 이후의 코드는 양보함 즉, yield까지 실행하고 멈춤
def 함수():
    print("출력A")
    yield 100
    print("출력B")
    yield 200
    print("출력C")
    yield 300
    print("출력D")
    yield 400
제너레이터 = 함수()
값1 = next(제너레이터)    # 첫 번째 yield인 100까지 실행하고 멈춤
print(값1)
값2 = next(제너레이터)    # 두 번째 yield인 200까지 실행하고 멈춤
print(값2)
값3 = next(제너레이터)    # 세 번째 yield인 300까지 실행하고 멈춤
print(값3)

# 제너레이터는 1회용 함수
for i in 제너레이터:
    print(i)

def 반전(리스트):
    for i in range(len(리스트)):
        yield 리스트[-i - 1]

제너레이터 = 반전([1, 2, 3, 4, 5])
for i in 제너레이터:
    print(i)