# 기본 코드 

import sys
sys.stdin = open("input.txt", "r")


# 2979 트럭주차

# input 값 
cost = list(map(int,input().split()))

# 24시간에 대한 빈 배열 생성
time_100 = [0 for j in range(100)]
#print(time_24)

for c in range(3):
    a,b = map(int,input().split())
    for cc in range(a,b) : 
        time_100[cc] += 1 
#print(time_100)
total_count = (time_100.count(1))*cost[0] + (time_100.count(2))*cost[1]*2 + (time_100.count(3))*cost[2]*3
print(total_count)



# 2675 자열 반복

T = int(input())
for t in range(1,T+1):
    R,S = input().split()
    new_string = ''
    for s in S: # 이렇게 하면 s는 S의 요소가 됨
        new_string += int(R)*s

    print(new_string)


# 1110 더하기 사이클

num = int(input())
N = num
count = 0 
while True :
    # divmod 
    lnum = num//10 # 2
    rnum = num%10  # 6
    lsnum = (rnum + lnum) %10 # 8 
    num = (rnum*10) + lsnum # 68
    count += 1
    if num == N:
        break
print(count)



# 1157 단어공부
string = input().upper()
strings = list(set(string))
#print(strings)
cnt_list = []

# count 쓰는 경우
for t in strings : # string에 있는 애들 내에서 
    cnt = string.count(t) # Mississipi
    cnt_list.append(cnt) 
print(cnt_list) # [1,1,4,4]

if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
else :
    max_index=cnt_list.index(max(cnt_list))
    print(strings[max_index])


# 1439 뒤집기

numbers = list(map(int,input()))

zero = []
one = []
cnt = 0
for i in range(int(len(numbers))-1): 
    if numbers[i] != numbers[i+1] :  
        cnt += 1  
print((cnt + 1) // 2)


# 7567 그릇

bowl = input() 
height = 10
for i in range(len(bowl)-1) :
    if bowl[i] != bowl[i+1]:
        height =  height + 10
    else : 
        height =  height + 5
print(height)

