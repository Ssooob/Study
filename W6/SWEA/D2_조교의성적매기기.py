# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split()) # N은 학생 수, K는 점수를 알고싶은 학생
    NN = N/10
    score = []
    total_score = {}
    for n in range(N):
        score.append(list(map(int,input().split())))
        total_score[n+1] = round((score[-1][0]*0.35) + (score[-1][1]*0.45)+(score[-1][2]*0.20),2)
    sort_score = sorted(total_score.items(),key = lambda x : -x[1])
    index= 0
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    for n in range(N):
        if n%NN == 0:
            index+=1
            #print(index)
        if sort_score[n][0] == K :
            print(f"#{t} {grade[index-1]}")
            break
