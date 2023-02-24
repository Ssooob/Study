# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

# 2525 오븐시계
'''
h, m = map(int,input().split())
time = int(input())
mm = m + time 

if mm > 59:
    hh = mm//60
    h += hh
    mm -= 60*hh
    if h > 23 :
        hhh = h//24
        h -= 24*hhh
print(h,mm)
'''

# 2798 블랙잭

from itertools import combinations, permutations

N,M = map(int,input().split())
numbers = list(map(int,input().split()))

#combi = list(combinations(numbers, 3))
combi_sum = list(map(sum,list(combinations(numbers, 3))))
min,idx = M,0
print(combi_sum)
for x in combi_sum:
    if x <= M :
        if M-x < min :
            min = M-x
            min_idx = idx
    idx += 1
print(combi_sum[min_idx])


# 점수 집계
'''
T = int(input())
for t in range(T) :
    
    score = list(map(int,input().split()))
    del score[int(score.index(max(score)))]
    del score[int(score.index(min(score)))]

    if max(score)-min(score) >=4 :
        print("KIN")
    else :
        print(sum(score))
'''


# 1526 가장 큰 금민수
