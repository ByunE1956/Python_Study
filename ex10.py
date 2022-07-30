# 딕셔너리 연습 1
#dictionary = {
#    "keyA" : "valueA",
#    "keyB" : "valueB",
#    "keyC" : "valueC"
#}

# 딕셔너리 연습 2
dictionary = {
    "문자열" : "안녕하세요",
    8834 : 1956,
    True : False
}

print(dictionary["문자열"])
print(dictionary[8834])
print(dictionary[True])

for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))

dictionary["리스트"] = [1,2,3,4]
print()
for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))

del dictionary["리스트"]
print()
for key in dictionary:
    print("{} : {}".format(key, dictionary[key]))