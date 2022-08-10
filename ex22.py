# flatten Function
def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output.extend(flatten(item))
        else:
            output.append(item)
    return output

example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))

# **list 연결 함수 부분 공부가 필요함