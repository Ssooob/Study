# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    matrix = []
    N,K = map(int,input().split())
    # matrix 생성
    for n in range(N):
        matrix.append(list(map(int,input().split())))
    result = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1 :
                cnt +=1
            if matrix[i][j] == 0 or j == N-1:
                if cnt ==   K:
                    result += 1
                cnt = 0
        
        for j in range(N):
            if matrix[j][i] == 1:
                cnt += 1
            if matrix[j][i] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt= 0
    print(f"#{t} {result}")


    # print(f"#{t} {grade[index-1]}")