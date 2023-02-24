# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

# 1547 공


# 5576 콘테스트
'''
W,K = [],[]
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))
Score_W = sorted(W,reverse=True)[0:3] 
Score_K = sorted(K,reverse=True)[0:3]
print(sum(Score_W),sum(Score_K))
'''

# 2846 오르막길
'''
N = int(input())
road = list(map(int,input().split()))
total_distance = []
distance = 0
for r in range(N-1):
    if road[r]<road[r+1]:
        distance += road[r+1]-road[r]
    else :
        total_distance.append(distance)
        distance = 0
total_distance.append(distance) # 마지막값
print(max(total_distance))
'''

# 1251 단어 나누기
voca = input()
len_voca = len(voca)
result = []
# 합이 7인 조합들
for i in range(1,len_voca-1):
    for j in range(i+1,len_voca):
        ans = (voca[:i][::-1])+(voca[i:j][::-1])+(voca[j:][::-1])
        result.append(ans)
result.sort()
print(result[0])

# 힙으로 푸는 방법




'''
voca = input()
len_voca = len(voca)
combination = []
# 합이 7인 조합들
for i in range(1,len_voca):
    for j in range(1,len_voca):
        for k in range(1,len_voca):
            if i + j + k == 7 :
                combination.append([i,j,k])
result = []
for v in range(len(combination)):
    seper = combination[v]
    sep_voca,rev_voca = [],[]
    a = 0
    for i in range(len(seper)): 
        b = seper[i] # 2 3 2 
        vocavoca = voca[a:a+b]
        sep_voca.append(vocavoca) # 01 234 56
        a = a+b
        rev_voca.append(vocavoca[::-1])
    rev_voca = "".join(rev_voca)
    result.append(rev_voca)
#print(sorted(result)[0])
print(min(result))
'''
