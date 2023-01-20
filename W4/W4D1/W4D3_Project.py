# 기본 코드
import sys
sys.stdin = open("input.txt", "r")


# 9498 시험성적
score = int(input())
if 90 <= score <= 100 :
    print('A')
elif 80 <= score <= 89 :
    print('B') 
elif 70 <= score <= 79 :
    print('C') 
elif 60 <= score <= 69 :
    print('D') 
else :
    print('F')


# 9093 단어 뒤집기
T = int(input())
for t in range(T):
    rs = ''
    string = list(input().split())
    for s in string :
        rs += s [::-1] + ' ' 
    print(rs)


# 11721 열 개씩 끊어 출력하기
string = input()
cnt = 0
for i in string:
    print(i,end='')
    cnt +=1
    if cnt == 10 :
        print()
        cnt = 0


# 2947 나무조각
ori_numbers = list(map(int,input().split()))
numbers = ori_numbers

while numbers != sorted(ori_numbers) :
    for i in range(len(numbers)-1):
        if numbers[i]> numbers[i+1] : 
            numbers2 = [numbers[i],numbers[i+1]]
            s_numbers2 = sorted(numbers2)   
            numbers [i] = s_numbers2[0]
            numbers [i+1] = s_numbers2[1]
            print(*numbers) 
        else :
            pass


# 그냥 값 치환으로도 됨
while numbers != sorted(ori_numbers) :
        for i in range(len(numbers)-1):
            if numbers[i]> numbers[i+1] : 
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                print(numbers)


