
#1 문자열을 받고 e가 처음 나오는 위치를 출력 
string = input()
for i in range(len(string)):
    if string[i] == 'e':
        print(i)
        break
else :
    print(-1)

#2 문자열을 입력받고, 각 단어의 등장 횟수를 출력 
# 이 때는 딕셔너리 쓰는게 좋음

string = input("입력:").split()
dict_var = {}

# count 안 쓸 때
# i는 종류 구분하기

for word in string:
    if word in dict_var :
        dict_var[word] += 1 
    elif word not in dict_var :
        dict_var[word] = 1

for key, value in dict_var.items():
    print(f"{key} {value}")


#3
string = input("문자열을 입력하세요 >")
result = ""

for i in string : 
    if i != 'e' :
        result += i 
print(result)


#4
string = input("문자열을 입력하세요 >").split()
# print(string)
num = 0
for i in string[0]:
    if i == string[1] :
        num += 1
print(num)


#5
string = input("문자열을 입력하세요 >").split()
# print(len(string))
new_string = string[0]

for i in range (1, len(string)):
    next_string = '-' + string[i] 
    new_string += next_string
print(new_string)


#6
num = int(input("양의 정수를 입력하세요 > "))
print(num(1))
sum = 0

if num < 0 :
    print(-1)
else :
    for i in range(num) :
        print(i)
        #sum += num[i] 
    #print(sum)


