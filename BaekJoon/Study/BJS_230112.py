# 기본 코드 

import sys
sys.stdin = open("input.txt", "r")

'''
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



# 문자열 반복

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
    lnum = num//10 # 2
    rnum = num%10  # 6
    lsnum = (rnum + lnum)%10 # 8 
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
for t in strings :
    cnt = string.count(t)
    cnt_list.append(cnt)
#print(cnt_list)

if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
else :
    max_index=cnt_list.index(max(cnt_list))
    print(strings[max_index])

'''  



'''
# count 타협한 경우..

for s in strings :
    if s not in num_dict:
        num_dict[s] = 1
    elif s in num_dict:
         num_dict[s] += 1
'''


'''
for i in range(len(num_dict.values())) :
    max = -100000
    same = []
    if num_dict.values(i) >  max :
        max = num_dict.values(i)
        max_idx = i
    elif i == max :
         same.apped(i)
print(max_idx)
print(same)


'''
'''
    if i :
        print(i)
    print
find_max = max()
print(num_dict.values() )
#for value in num_dict.values():
 #   print(f"{value}")''' 


