"""
파일을 다루기
- 쓰기
 - 새로(write): w
 - 있는 파일 뒤에(append): a
- 읽기(read): r
"""

file = open("test.txt", "a")
file.write("Hello")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

# 위의 구문과 동일하게 작동한다.
with open("test.txt", "a") as file:
    file.write("Hello!")