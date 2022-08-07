def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)

# 가변매개변수는 앞에 적을수 없음
# 가변매개변수는 딱 하나만 사용할 것
def 가변매개변수함수(매개변수1, 매개변수2, *가변매개변수):
    print(매개변수1)
    print(매개변수2)
    print(가변매개변수)

가변매개변수함수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 디폴트 값을 설정하는 매개변수를 기본매개변수라고 한다.
# 해당 경우 매개변수를 지정하지 않으면 설정한 디폴트 값이 들어간다
# 기본매개변수는 매개변수 앞에 선언 할 수 없다
def print_n_times2(value, n=3):
    for i in range(n):
        print(value)

print_n_times2("안녕하세요")