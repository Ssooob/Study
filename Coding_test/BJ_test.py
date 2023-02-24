# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline


# 바이러스
'''
m = int(input())
n = int(input())
comp = [[]for _ in range(m+1)]
# print(comp)

for _ in range(n):
    v1,v2 = map(int,input().split())
    comp[v1].append(v2)
    comp[v2].append(v1)
# print(comp)

attack_comp = []
def dfs(start,visited):
    visited[start] = 1
    for i in comp[start] : 
        if visited[i] == 0:
            dfs(i,visited)

visited = [0]*(m+1) 
dfs(1,visited)
print(sum(visited)-1)
'''