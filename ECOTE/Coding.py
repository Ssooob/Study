# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

# # 10773 제로
'''
# # 가장 최근에 넣은 값을 가장 빨리 꺼낸다 -> 스택
N = int(input())
stack_list = []
for i in range(N):
    num = int(input())
    if num == 0 :
        stack_list.pop()
    else :
        stack_list.append(num)
print(sum(stack_list))
'''
'''
# 2161 카드1
# 데큐로 풀면 더 빠름
from collections import deque

N = int(input())
numbers = deque(range(1,N+1))
while len(numbers)>1:
    print(numbers.popleft(),end="")
    numbers.append(numbers.popleft())
print(numbers[0])
'''

# 동적 프로그래밍 DP
# 피보나치 수열처럼.. 앞쪽 계산 값이 뒤 쪽의 값에 영향을 줄 때.. 점화식을 세울 수 있으면 DP로 푸는 것이 좋음

# 1로 만들기
d = [0]*30001


# 개미 전사
'''
N = int(input())
food = list(map(int,input().split()))
# 핑퐁임 1010 or 0101
onezero = [0]*N
fc1,fc2 = 0,0
for i in range(N):
    if i % 2 == 0 :
        onezero[i] = 1
    fc1 += food[i]*onezero[i] 
onezero = [0]*N
for j in range(4):
    if j % 2 == 1:
        onezero[j] = 1
    fc2 += food[j]*onezero[j]

print(max(fc1,fc2))
'''
'''
# 얘의 경우.. 더한 값을 따로 DP에 저장해놓는 것
n = int(input())
array = list(map(int,input().split()))
d = [0]*100 

d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])


# 털지 안 털지에 대한 여부를 경우
# 바로 앞쪽에서 창고를 털었다면, 다음 창고는 못 털고
# 안 털었으면 털 수 있음

# 최적 부분 구조 -> 특정
# 큰 문제를 활용하기 위해 작은 문제 두개를 이용할 수 있음

'''

# DFS 소스코드 예제
'''
# DFS 메서드 정의
def dfs(graph,v,visited):
    # 현재 노드를 방문처리
    visited[v] = True # 1번에 대한 방문 처리 
    print(v,end = ' ')

    for i in graph[v]: # 인접한 리스트로 접근 
        if not visited[i] : # False면 
            dfs(graph,i,visited) # 다시 해당 값을 방문처리 할 수 있게

# 그래프 2차원 리스트 선언
graph = [
    [], # 보통 리스트 1부터 하는 경우가 많음 0은 비워두기
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
] 

visited = [False]*9 # 0부터니까 +1 한 갯수로 방문 여부 확인하기
dfs(graph,1,visited) # list 1부터 확인 
'''

# BFS 구현 예시
'''
from collections import deque

def bfs(graph, start, visited):
    # deque 라이브러리 사용
    queue = deque([start])

    visited[start] = True

    while queue : # 큐가 빌때까지 반복
        # 선입선출로 하나 뽑기 
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]: # False 라면
                queue.append(i)
                visited[i] = True

graph = [
    [], # 보통 리스트 1부터 하는 경우가 많음 0은 비워두기
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
] 
visited = [False]*9 # 0부터니까 +1 한 갯수로 방문 여부 확인하기
bfs(graph,1,visited) # list 1부터 확인 
'''

# 문제풀이
# 음료수 얼려먹기
'''
# 연결 요소의 갯수 - 상하좌우 인접한 것으로 표현할 수 있음

# 상하좌우를 살펴본 뒤, 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면
# 연결된 모든 지점을 방문
# 방문하지 않은 지점의 수를 카운트

# DFS로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어날 수 없음
    if x <=-1 or x >=n or y <=-1 or y >= m :
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        graph[x][y] == 1 # 방문 처리 해주고

        # 상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y) 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True 
    return False


# 입력받기
n,m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드에 대해서 음료수 채우기
result = 0 
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True :
            result +=1
print(result)

'''

# 미로 탈출
n,m = map(int,input().split())
graph = [[list(map(int,input().rstrip()))]for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS로 해보기
from collections import deque 

def bfs(x,y):
    queue = deque() # 재귀가 아니라, bfs 한 번 수행하는거라 함수 안 쪽에 queue 선언
    queue.append((x,y)) # x,y 좌표를 tuple로 담음

    # 큐가 빌 때까지 bfs를 수행
    # BFS : 먼저 제일 앞에 있는 애를 넣고, 큐에서 뺌, 그리고 그 주변 노드들을 다 큐에 넣음
    # 그리고 제일 인접한 애를 큐에서 빼고, 그 주변 노드들을 다 큐에 넣는 것을 반복
    # 그렇게 해서 다 방문 처리를 했기 때문에 큐가 비면 모든 노드들을 다 탐색했다는 소리 

    while queue : # 큐가 빌 때까지 반복하기
        x,y = queue.popleft()
        for i in range(4) : # 4가지 방향
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어났을 경우는 무시
            if nx < 0 or nx >=n or ny < 0 or ny >= m :
                continue
            # 괴물 있는 곳
            if graph[nx][ny] == 0 :
                continue

            # 갈 수 있는 곳
            if graph[nx][ny] == 1 :
                graph[nx][ny] == graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))



# 이동할 네 가지 방향 정의(상,하,좌,우)



# print(graph)

# for _ in range(n):
#     graph.append(list(map(int,input().rstrip())))


