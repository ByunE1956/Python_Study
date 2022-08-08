# start~end까지 있는 모든 정수를 더하는 함수
def sum_all(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
    return result

print(sum_all(1, 100))
print(sum_all(50, 100))

def f(x):
    return 2*x+1
print(f(10))

def f2(x):
    return x**2+2*x+1
print(f2(10))

def mul(*values):
    result = 1
    for i in values:
        result *= i
    return result
print(mul(5, 7, 9, 10))