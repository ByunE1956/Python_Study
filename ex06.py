import datetime

now = datetime.datetime.now()

#if now.hour < 12:
#    print("현재 시간은 {}시 {}분으로 오전입니다!".format(now.hour, now.minute))
#if now.hour >= 12:
#    print("현재 시간은 {}시 {}분으로 오후입니다!".format(now.hour, now.minute))

#if 3 <= now.month <= 5:
#    print("이번 달은 {}월로 봄입니다.".format(now.month))
#if 6 <= now.month <= 8:
#    print("이번 달은 {}월로 여름입니다.".format(now.month))
#if 9 <= now.month <= 11:
#    print("이번 달은 {}월로 가을입니다.".format(now.month))
#if now.month == 12 or 1 <= now.month <= 2:
#    print("이번 달은 {}월로 겨울입니다.".format(now.month))

number = input("정수를 입력해주세요: ")

last_character = number[-1]

# <문자열로 하나씩 계산>
#last_character = int(last_character)
#if last_character == 0 or last_character == 2 or last_character == 4 \
#    or last_character == 6 or last_character == 8:
#    print("짝수입니다")
#if last_character == 1 or last_character == 3 or last_character == 5 \
#    or last_character == 7 or last_character == 9:
#    print("홀수입니다")

# <문자열로 계산 in 사용>
#if last_character in "02468":
#    print("짝수입니다")
#if last_character in "13579":
#    print("홀수입니다")

# <실제 자주 사용>
number = int(number)
if number % 2 == 0:
    print("짝수입니다")
if number % 2 == 1:
    print("홀수입니다")