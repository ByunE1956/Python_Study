import time
from tracemalloc import start

i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()

numbers = [1, 2, 1, 2, 1, 2, 1, 2]

while 1 in numbers:
    numbers.remove(1)
    print(numbers)

start_time = time.time()
print(start_time)
while start_time + 5 >= time.time():
    pass
print("프로그램이 종료되었습니다.")