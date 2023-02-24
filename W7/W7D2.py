import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline


# 17608 막대기 (92ms)
'''
input = sys.stdin.readline # 시간초과
T = int(input())

bars = []
for _ in range(T):
    bars.append(int(input()))
max_bar = bars[-1]
reverse_bar = bars[::-1]
cnt = 1
for b in reverse_bar:
    if b > max_bar :
        cnt += 1
        max_bar = b  
print(cnt)
'''

# 7568 덩치 (48ms)
# 키와 몸무게와 덩치
# 1:1로 비교하는 것이 아닌, 본인보다 키 & 몸무게가 크고 많이 나가는 사람의 수를 세는 것

T = int(input())
members = []
for _ in range(T):
    my_w,my_h = map(int,input().split())
    members.append((my_w,my_h)) # 자구 리스트 내 값이 변해서.. tuple로 풀었음
for i in range(T):
    my_data = members[i]
    rank = 1
    for j in range(T):
        #print(my_data[0], members[j][0])
        #print(my_data[1], members[j][1])
        if my_data[0] < members[j][0] and my_data[1] < members[j][1]:
            #print('**')
            rank += 1 
    print(rank, end = " ")



# for i in range(len(members)): # member는 기존 
#     #print(i)
#     #print(members)
#     vari_member = members # 처음은 member로 초기화
#     my_w,my_h = members[i][0],members[i][1] # 나의 데이터를 뽑음

#     # 나를 제외한 다른 사람들의 데이터 저장
#     vari_member.remove(vari_member[i])
#     print(members)
#     print(vari_member)

#     #for j in range(members):
#         # 나와 다른 사람들을 비교

