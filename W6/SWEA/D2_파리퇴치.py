# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_death= 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            death = 0
            for di in range(M):
                for dj in range(M):
                    death += matrix[i+di][j+dj]
            if death > max_death :
                max_death = death
    print(f"#{t} {max_death}") 
