# 기본 코드 
import sys
#input = sys.stdin.readline
sys.stdin = open("input.txt", "r",encoding='UTF8') # ,encoding='UTF8'


# 17484 진우의 달 여행 (small)
'''
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

MAX_VAL = 100 * 1000 + 1 # 아예 큰 값
dp = [[[MAX_VAL]*3 for _ in range(M)] for _ in range(N)]
print(dp)

for y in range(N):
    if y == 0:
        for x in range(M):
            for d in range(3):
                dp[y][x][d] = board[y][x]
    else:
        for x in range(M):
            # 오른쪽 밑으로 오지 않음
            if x == 0:
                dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + board[y][x]
                dp[y][x][1] = dp[y-1][x][0] + board[y][x]
            # 왼쪽 밑으로 오지 않음
            elif x == M-1:
                dp[y][x][1] = dp[y-1][x][2] + board[y][x]
                dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + board[y][x]
            else:
                dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + board[y][x]
                dp[y][x][1] = min(dp[y-1][x][0], dp[y-1][x][2]) + board[y][x]
                dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + board[y][x]
answer = 1e9
for x in range(M):
    answer = min(min(dp[N-1][x]), answer)
print(answer)

'''
#input = sys.stdin.readline
'''
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]
# bool 형 말고, 계산할 수 있는 무언가 

# print('dp',dp)
for i in range(1,N+1): # 1부터 
    for j in range(M): # 4개씩 비교 0,1,2,3
        # 왼쪽 아래, 아래, 오른쪽 아래

        # 왼쪽으로 내려갈 때 사용량
        if j < M-1: # 2 1 0 
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + matrix[i-1][j]
        
        # 오른쪽으로 내려갈 때 사용량 
        if 0 < j: # 1 2 3 
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + matrix[i-1][j]
        
        # 수직으로 내려갈 때 사용량
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + matrix[i-1][j]

        print(dp)
min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value,each)
print(min_value)

'''


n, m = map(int, input().split())
MAX = 100*1000
# 연료 사용 첫 줄
dp = [[MAX]*3] + [[el]*3 for el in list(map(int, input().split()))] + [[MAX]*3]
print(dp)

# n-1줄 연료를 받아옴
for i in range(n-1):
    # 연료량
    fuel = [MAX]+list(map(int, input().split()))+[MAX]
    #print('fuel',fuel)
    # 다음 연료 사용량 목록 
    tmp = [[MAX]*3] + [[0]*3 for _ in range(m)] + [[MAX]*3]
    #print('tmp',tmp)
    
    # tmp 양 끝단을 MAX처리 
    for j in range(1, m+1): # j는 1부터 양단을 max 값으로 해주었으니
        #print('dp',dp)
        
        #왼쪽으로 내려갈 때 사용량
        # 중복이 안되기 때문에 수직, 오른쪽만 계산 
        #현 시점에서 오른쪽 상단 위치에서 min(수직으로 내려온 값, 오른편으로 내려온 값) + 현재 연료량
        tmp[j][0] = min(dp[j + 1][1], dp[j + 1][2]) + fuel[j]
        
        #수직으로 내려갈 때 사용량
        #현 시점에서 수직 상단 위치에서 min(오른쪽으로 내려온 값, 왼쪽으로 내려온 값) + 현재 연료량
        tmp[j][1] = min(dp[j][0], dp[j][2]) + fuel[j]
        
        #오른쪽으로 내려갈 때 사용량
        #현 시점에서 왼쪽 상단 위치에서 min(왼쪽으로 내려온 값, 수직으로 내려온 값) + 현재 연료량
        tmp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + fuel[j]
        #print('tmp',tmp)
        
    # 상단 값 갱신후 반복
    dp = tmp

# 마지막 연료량 중 최솟값 출력
print(min(map(min, dp)))

'''
r,c = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(r)]
dp = [0]*3
dp = [0]*r
dp [0] = min(matrix[0])
dp_idx = matrix[0].index(min(matrix[0]))
move = [-1,0,1]
next_move = []
print(dp_idx)

for i in range(r):
    # 내려갈 수 있는 경우의 수
    next_move = []
    for m in move:  
        next_idx = dp_idx+m
        print(next_idx)
        if next_idx >= 0 and next_idx < c :
            next_move.append(m) 
    # 이전과 겹치면 안됨 
    if next_move in move:

'''
    
# 사실상 무조건 for문으로 6줄은 돌거고.. 
# 조건은 열에 있는건데..
# 내가 선택할 수 있는 경우의 수? 
# if 2 -> 1 / 2 / 3 
# if 3 -> 1 / 2
# 만약.. 

# for i in range(1,r+1):
#     # 비교 대상 배열 만들고
#     comp = []
#     dp[i] = min(comp)

'''
# 1316 그룹 단어 체커
T = int(input())
cnt = 0
for t in range(T):
    voca = input()
    alp = [0]*26 
    break_point = False
    for v in range(len(voca)) :
        if alp[ord(voca[v])-ord('a')] == 0 :
            alp[ord(voca[v])-ord('a')] += 1
            continue
        elif alp[ord(voca[v])-ord('a')] != 0 and voca[v-1] == voca[v] :
            continue
        elif  alp[ord(voca[v])-ord('a')] != 0 and voca[v-1] != voca[v] :
            break_point = True
            break
    if break_point == False :
        cnt += 1
print(cnt)
'''

# 2578 빙고 
'''
matrix = [list(map(int,input().split())) for _ in range(5)]
test = [list(map(int,input().split())) for _ in range(5)]
bingo = [[0]*5 for _ in range(5)]
bingo3 = 0
break_point = False


for i in range(5):
    for j in range(5):
        point = test[i][j]
        # 숫자 찾기 
        for k in range(5):
            #print(point)
            if point in matrix[k] :
                point_idx = matrix[k].index(point)
                bingo[k][point_idx] = 1
        
        #print(bingo)
        # 빙고세기
        bingo1,bingo2,bingo3,bingo4 = 0,0,0,0
        
        # 한 행이 빙고
        for u in range(5):
            if sum(bingo[u]) == 5 :
                bingo3 += 1
                #print('row',bingo3)
            if sum(list(zip(*bingo[::-1]))[u]) == 5 :
                bingo3 += 1
                #print('col',bingo3)
  
        # 대각선 빙고 
        down_cross,up_cross = 0,0 
        for u in range(5):
            down_cross += bingo[u][u]    
            if down_cross == 5 :
                #print('dc',down_cross) 
                bingo3 += 1
                #print('+',bingo3)
            up_cross += bingo[4-u][u]
            #print(bingo[4-u][u], end = '')
            if up_cross  == 5 :
                #print('uc',up_cross) 
                bingo3 += 1
                #print('-',bingo3)
        #sum_bingo = bingo1+bingo2+bingo3+bingo4 
        #print('sum_bingo',sum_bingo)
        # 빙고 3개 ! 
        if bingo3 == 3 :
            break_point = True
            #print(point)
            #print(bingo)
            total_sum = 0 
            for b in range(5):
                total_sum += sum(bingo[b])
            break
        if break_point == True : break
    if break_point == True : break

    # 총합 빙고 구하기 
print(total_sum)       

'''