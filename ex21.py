# n! = 1 * 2 * 3 * 4 * ... * n
def factorial_1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial_1(4))

# n! = n * (n-1) * .... * 1
def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n-1)
print(factorial_2(4))



# f(1) = 1, f(2) = 1
# f(n) = f(n-1) + f(n-2)
counter = 0
def fibonaci(n):
    # 함수 외부에 선언된 변수를 사용할 때에는 global이라고 명시를 해야함
    global counter
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)
print(fibonaci(10))
print(counter)
counter = 0

# memoization
memo = {1:1, 2:1}
def f(n):
    global counter
    counter += 1
    if n in memo:
        return memo[n]
    else:
        output = f(n-1) + f(n-2)
        memo[n] = output
        return output
print(f(40))
print(counter)

# 조기리턴
def f(n):
    if n in memo:
        return memo[n]
    # 윗 부분에서 리턴이 이뤄지므로 위의 f함수와 실행 결과는 똑같음
    # But 파이썬에서는 들여쓰기를 최소화하는 것이 좋은 코드이므로 else를 빼서 들여쓰기 단계를 축소시킴
    output = f(n-1) + f(n-2)
    memo[n] = output
    return output