'''
#1 문자열을 받고 e가 처음 나오는 위치를 출력 
string = input()
for i in range(len(string)):
    if string[i] == 'e':
        print(i)
        break
else :
    print(-1)
'''

#2 문자열을 입력받고, 각 단어의 등장 횟수를 출력 
# 이 때는 딕셔너리 쓰는게 좋음

string = input().split()
dict_var = {}

# count 안 쓸 때
# i는 종류 구분하기
for word in string:
    if word in dict_var :
        dict_var[word] += 1 
    elif word not in dict_var :
        dict_var[word] = 1

#for key, value in dict_var.itens():
    
   

# count 쓸 때
'''
for i in range(len(string)):
   ''' 