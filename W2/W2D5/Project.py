my_list = ['서울','서울','대전','광주','서울','대전','부산','부산']

my_set = set(my_list)

print(my_set)
print(len(my_set))

# set 안 쓰고 풀었을 경우
locations =['서울','서울','대전','광주','서울','대전','부산','부산']
result = []

for location in locations :
    if location not in result :
        result.append(location)
print(result)
print(len(result))



