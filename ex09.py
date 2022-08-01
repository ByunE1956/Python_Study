#a = [1, 2, 3, 4, 5, 6, 7]
#
#for element in a:
#    print(element)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print("- 100 이상의 수:", number)
print("=" * 30)

for number in numbers:
    if number % 2 == 0:
        print("{}는 짝수입니다.".format(number))
    else:
        print("{}는 홀수입니다.".format(number))
print("=" * 30)

for number in numbers:
    print("{}는 {}자리수입니다.".format(number, len(str(number))))
print("=" * 30)

list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

for i in list_of_list:
    for j in i:
        print(j)
print("=" * 30)

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers2:
    output[(number - 1) % 3].append(number)
print(output)

