array = []

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for i in range(0, 20, 2):
    array.append(i * i)
    # [0, 4, 16, 36, 64, 100, 144.....]
print(array)

# 위에 있는 for 문이 간단하네 구현가능
array = [i * i for i in range(0, 20, 2)]
print(array)

array_1 = [i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array_2 = [i for i in range(0, 10, 2)]
# [0, 2, 4, 6, 8]
array_3 = [1 for i in range(10)]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(array_1)
print(array_2)
print(array_3)

# if 문으로  조건도 넣을 수 있음
array_4 = [i for i in range(10) if i % 3 == 0]
print(array_4)


# 확인 문제
output = [i for i in range(1, 100 + 1, 1) if "{:b}".format(i).count("0") == 1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))