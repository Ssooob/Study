# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline


# 1012 유기농 배추
# DFS로 풀어야징
import sys
sys.setrecursionlimit(10000)
t = int(input())
for T in range(t):
    n,m,p = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(p):
        v1,v2 = map(int,input().split())
        graph[v1][v2] = 1

    def dfs(x,y):
        # 특정한 노드를 방문한 뒤에 연결된 노드들도 방문

        # 주어진 위치 이외 곳을 방문한다면 종료
        if x <=-1 or x >=n or y <=-1 or y >= m :
            return False

        # 현재 노드를 방문하지 않았다면 
        if graph[x][y]== 1 :
            # 해당 노드 방문 처리
            graph[x][y] = 0

            # 상,하,좌,우 모두 재귀적으로 호출
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            # 연결된 모든 위치에서 방문처리를 하기 위해 재귀적으로 dfs 호출 -> 이는 return 값을 사용하지 않기 때문ㅇ
            # 단순히 연결된 노드에 대해 방문처리에 대한 용도로 활용
            return True 
            # 결과적으로 True 값을 반환할 수 있도록 해서 현재 위치에서 dfs가 수행된 것이기 때문에 그 위치에 대해서 result값을 증가시킴
        return False
        # 방문하지 않은 곳이라면 True / 방문 했던 곳이라면 False

    # 모든 노드에 대해 탐색
    result = 0 
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i,j) == True : # 방문처리가 된 것이라면 
                result += 1
    print(result)

    # 해당 위치에 대해 한 번 dfs를 수행하면, 모든 위치에 대해서 방문 처리를 수행할 수 있게 함 
    # 그 시작점이 처음 방문하는 것이라면, 그 때만 result 값을 증가시킴




# [참고] https://hei-jayden.tistory.com/100

# 1389 케빈 베이컨의 6단계 법칙
# BFS로 풀어볼까?

'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start,visited,connection):
    queue = deque()
    queue.append(start)

    while queue :
        a = queue.popleft()
        visited[a] = True
        for i in friends[a] :
            if visited[i] == False :
                visited[i] = True
                connection[i] = connection[a] + 1
                queue.append(i)
    return sum(connection)

N,M = map(int,input().split())
friends = [[]for _ in range(N+1)]
for _ in range(M):
    v1,v2 = map(int,input().split())
    friends[v1].append(v2)
    friends[v2].append(v1)

result = []
for k in range(1,N+1):
    visited = [False]*(N+1)
    connection = [0]*(N+1)
    result.append(bfs(k,visited,connection))

print(result.index(min(result))+1)

'''


# 16173 점프왕 젤리(SMALL)
'''
import sys
from collections import deque
input=sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    buff = list(map(int,input().split()))
    graph.append(buff)

# 방문 기록 만들기
visited=[]
for _ in range(N):
  visited.append([0 for _ in range(N)])

def bfs(x,y,graph):
    queue = deque()
    queue.append((x,y)) # 큐에 넣고 

    while queue : # 큐가 빌 때까지 
        x,y = queue.popleft() # 뺌
        visited[x][y]=1 # 방문 기록 
        W = graph[x][y] # 초기 값 
        dx = [W, 0]
        dy = [0, W]

        # 2개에 대한 방향
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어났을 경우는 무시 
            if 0 > nx or nx >= N or 0 > ny or ny >= N :
                continue
            if visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                queue.append((nx,ny))

bfs(0,0,graph)

if visited[N-1][N-1]== 1: # 마지막에 방문할 수 있으면 
  print("HaruHaru")
else:
  print("Hing")
'''

# 26169 세번 이내에 사과를 먹자
'''
graph,visited = [],[]
for _ in range(5):
    graph.append(list(map(int,input().split())))
    visited.append([False]*5)
x0,y0 = map(int,input().split())

for i in range(5):
    for j in range(5):
        if graph[i][j] == -1:
            visited[i][j] = True

# print(visited)
# print(graph)
#print(x0,y0)

# 뭘로 풀지? -> dfs?

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def dfs(x,y,visited,step):
    # 방문한 곳에 대한 방문처리 
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 공간을 벗어났을 경우는 무시 
        if nx < 0 or nx >=5  or ny < 0 or ny >=5 :
            continue
        # 간 곳 외엔 다른 방향으로 못 감
        direc = [0,1,2,3]
        direc.pop(i)
        for j in direc :
            if x + dx[j] < 0 or x + dx[j] >=5  or y + dy[j] < 0 or y + dy[j] >=5 :
                continue
            else :
                visited[x + dx[j]][y + dy[j]] = True 
            
        # 3번 이전에 2개 먹었을 경우 
        if step - ((step//1000)*1000) == 3 :
            return step

        # 사과 및 다음 방문 처리 할 함수 호출
        if visited[nx][ny] == False :
            step += 1
            visited[nx][ny] == True
            if graph[nx][ny] == 1 :
                step += 1000 
            dfs(nx,ny,visited,step)

result  = dfs(x0,y0,visited,0)
if (int(result)//1000) >= 2 :
    print(1)
else :
    print(0)
'''

# 2468 안전영역
'''
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

N = int(input())
graph = []
max_buff,min_buff = [],[]
for _ in range(N):
    buff = list(map(int,input().split())) # 그리고 물에 잠기지 않는 안전한 영역의 최대 개수 -> 이건 다 잠기면 안된다는 의미인 듯..
    max_buff.append(max(buff)) # 원래는 min도 했었는데.. 아예 잠기지 않을 수 있다의 의미는 0을 의미하는 듯
    graph.append(buff) 
max_val = max(max_buff)

def dfs(x,y,visited):
    if x <=-1 or x >=N or y <=-1 or y >= N :
        return False

    # 현재 노드를 아직 방문하지 않았다면?
    if visited[x][y] == 0 :
        # 해당 노드 방문 처리
        visited[x][y] = 1
        # 상,하,좌,우 재귀적으로 호출
        dfs(x+1,y,visited)
        dfs(x,y+1,visited)
        dfs(x-1,y,visited)
        dfs(x,y-1,visited)
        return True
    return False

# 잠긴부분 1 안 잠긴 부분 0으로 만들기 
total_result = []
for th in range(0,max_val): # 0부터(안 잠길 수도 있음), 최대 높이 -1 (다 잠기면 안됨)
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] <=th:
                visited[i][j] = 1
    #print(th, visited)
    # 모든 노드에 대해서  
    result = 0 
    for i in range(N):
        for j in range(N):
            if dfs(i,j,visited) == True:
                result += 1
    total_result.append(result)
#print(total_result)
print(max(total_result))

'''

# 7576 토마토
# 흠.. 이건 bfs가 더 편할 듯.. 
'''
from collections import deque
m,n = map(int,input().split())

# 2차원 그래프 받기 
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)

# 4 방향으로 나갈 수 있게 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 정답이 담길 변수
result = 0

def bfs(): # 원래는.. 시작점을 넣어야하는데, 시작점이 여러개인 경우가 있어서 뺐음
    # 큐 만들기 
    queue = deque()
    # 토마토 시작점 찾기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])

    while queue :
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 안되고, 빈공간도 안됨 
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익히고, 이전꺼에 1을 더해서 나오기 
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx,ny))

bfs()
for i in graph: # 리스트 
    for j in i: # 리스트 당 한 원소 
        # 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0) # 아예 나가버리기 
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(i))
# 처음 시작을 1로 표현했으니 1을 뺌
print(result - 1)

'''