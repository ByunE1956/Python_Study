# range(시작, 끝, 단계)
# range(시작, 끝) > 단계=1 생략
# range(끝) > 시작=0, 단계=1 생략

# 정순 출력
#for i in range(0, 10, 1):
#    print(i)

# 역순 출력
for i in reversed(range(10)):
    print(i)

array = [273, 52, 103, 32, 57]

i = 0
#for element in array:
#    print("{} : {}".format(i, element))

for i in range(len(array)):
    print("{} : {}".format(i, array[i]))
