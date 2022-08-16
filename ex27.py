numbers = [1, 2, 3, 4, 5, 6]

print("::".join(map(str, numbers)))

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda number: number % 2 != 0, numbers)))
print()

print("# 3이상, 7미만 추출하기")
print(list(filter(lambda number: 3 <= number < 7, numbers)))
print()

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda number: number ** 2 < 50, numbers)))