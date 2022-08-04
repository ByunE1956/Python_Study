# min 함수
#print(min([273, 52, 32, 57, 103]))

# max 함수
#print(max([273, 52, 32, 57, 103]))

# sum 함수 *반드시 리스트여야함
#print(sum([273, 52, 32, 57, 103]))

# reversed 함수 *1회용 함수로 한번 사용하고 나면 해당 변수는 초기화됨
#a = [0, 1, 2, 3, 4, 5]
#reversed_a = reversed(a)
#print(list(reversed_a))    # 출력 : [5, 4, 3, 2, 1, 0]
#print(list(reversed_a))    # 출력 : []

# enumerate 함수 *1회용 함수
a = [273, 52, 32, 57, 103]
print(list(enumerate(a)))       # 출력 : [(0, 273), (1, 52), (2, 32), (3, 57), (4, 103)]

for i, element in enumerate(a):
    print("{}번째 요소는 {}입니다.".format(i, element))

# items 함수
a = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3"
}
for key, value in a.items():
    print("{}키의 값은 {}입니다.".format(key, value))