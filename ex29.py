from operator import index


while True:
    try:
        print(float(input("> 숫자를 입력해주세요: ")) ** 2)
        break
    except:
        print("숫자를 입력해주세요!")

list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []

for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

numbers = [52, 273, 32, 103, 90, 10, 275]
print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 273
if number in numbers:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
else:
    print("- 리스트 내부에 없는 값입니다.")
print()

print("# (3) 요소 내부에 찾기 try except 구문사용")
number = 32
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except:
    print("- 리스트 내부에 없는 값입니다.")

print("--- 정상적으로 종료되었습니다. ---")