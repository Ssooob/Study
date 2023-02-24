# 기본 코드 
import sys
#input = sys.stdin.readline
sys.stdin = open("input.txt", "r",encoding='UTF8') # ,encoding='UTF8'

# 8979 올림픽

contry,score = map(int,input().split())
rank = []
for c in range(contry) :
    rank.append(list(map(int,input().split())))
# 금은동 순으로 정렬
sorted_rank = sorted(rank,key = lambda x : (-x[1],-x[2],-x[3]))
# 내가 찾는 국가가 몇 번째로 정렬되어있는지 모름
for i in range(contry):
    if sorted_rank[i][0] == score:
        index = i
# 특정 국가의 메달 조건이랑 정렬된 국가들의 메달 조건이 같은 i를 출력
# 어차피 같다고 쳐도 1등부터 나열하는 것이기 때문에 2,3... 등의 첫번째 값으로 출력될 것
# 그리고 동등수가 앞쪽에 있다고해도, 순번으로는 달라지는게 없음 
for i in range(contry):
    if sorted_rank[index][1:] == sorted_rank[i][1:]:
        print(i+1)
        break

# 1417 국회의원 선거

# sort 쓴 경우 (시간 48ms)
c = int(input())
candidate = []
for i in range(c):
    candidate.append(int(input()))
if len(candidate) > 1 :    
    mine,others = candidate[0],candidate[1:]
    vote = 0
    sorted_others = sorted(others,reverse=True) # 제일 많은 투표수 애를 깎아야하니..
    while True:
        sorted_others.sort(reverse=True) # for문 돌리면서 계속 최대값을 바꿔주어야함 
        if mine <= sorted_others[0]:
            mine +=1
            sorted_others[0] -=1 # 제일 큰 애에서 1씩 빼주고
            vote +=1 # 몇 번 뺏는지
        else:
            break 
    print(vote)
else :
    print(0)

# max 쓴 경우 (64ms)
c = int(input())
candidate = []
for i in range(c):
    candidate.append(int(input()))
if len(candidate) > 1 :    
    mine,others = candidate[0],candidate[1:]
    vote = 0
    while True:
        if mine <= max(others):
            mine +=1 
            others[others.index(max(others))]-=1
            vote +=1
        else:
            break 
    print(vote)
else :
    print(0)


# 1244 스위치 켜고 끄기

sw_num = int(input())
sw_state = list(map(int,input().split()))
N = int(input())
student =[]
for _ in range(N):
    student.append(list(map(int,input().split())))

def change(num):
    if sw_state[num] == 0:
        sw_state[num] = 1
    else :
        sw_state[num] = 0
    return 

for n in range(N):
    # 남학생일 경우
    if student[n][0] == 1:
        # 배수를 구하고, 해당 스위치의 상태를 변경
        for nn in range(student[n][1],sw_num+1,student[n][1]):
            change(nn-1)
        #print("남학생")
        #print(sw_state)
        #print("=============")

    # 여학생일 경우
    elif student[n][0] == 2:
        # 본인꺼 바꾸기 
        change(student[n][1]-1)
        #print("여학생")
        #print(sw_state)
        #print("=============")

        # 대칭에 대한거 변경 
        even = min(sw_num-student[n][1],student[n][1]-1)
        for e in range(1,even+1):
            #print(student[n][1]-1)
            if sw_state[student[n][1]-e-1]==sw_state[student[n][1]+e-1]:
                print(student[n][1]-e-1,student[n][1]+e-1)
                change(student[n][1]-e-1)
                change(student[n][1]+e-1)
            #print(sw_state)
            #print("=============")
        

# 20개 출력
count = 0
while count < len(sw_state):
    print(sw_state[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1

'''
for n in range(N):
    # 남학생일 경우
    if student[n][0] == 1:
        for nn in range(student[n][1],sw_num+1,student[n][1]):
            change(nn-1)

        num = []
        # 배수를 구하고, 해당 스위치의 상태를 변경
        for nn in range(student[n][1],sw_num+1,student[n][1]):
            if sw_state[nn-1] == 0:
                sw_state[nn-1] = 1
            else :
                sw_state[nn-1] = 0
        #print(sw_state)
        #print("=============")
    # 여학생일 경우
    elif student[n][0] == 2:
        flag = 0
        even = min(sw_num-student[n][1],student[n][1]-1)
        for e in range(1,even+1):
            #print(student[n][1]-1)
            if sw_state[student[n][1]-e-1]==sw_state[student[n][1]+e-1]:
                flag =1
                #print("+++")
                if sw_state[student[n][1]-e-1] == 0:
                    sw_state[student[n][1]-e-1] = 1
                    sw_state[student[n][1]+e-1] = 1
                else :
                    sw_state[student[n][1]-e-1] = 0
                    sw_state[student[n][1]+e-1] = 0
                #print(sw_state)
        if flag == 1:
            #print(sw_state[student[n][1]-1])
            if sw_state[student[n][1]-1] == 0:
                sw_state[student[n][1]-1] = 1
            else : 
                sw_state[student[n][1]-1] = 0
            #print(sw_state)
# 20개 출력
count = 0  
while count < len(sw_state):

    print(sw_state[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1
'''



# 2108 통계학
N = int(input())
numbers = []
freq_numbers={}
for n in range(N) :
    numbers.append(int(input()))

# 최빈값을 구하기 위한 코드
for i in set(numbers):
    freq_numbers[i] = numbers.count(i)
max_count = max(freq_numbers.values())
filt_numbers = dict(filter(lambda x : x[1] == max_count,freq_numbers.items()))
sort_filt_numbers =  sorted(filt_numbers.items(),key=lambda x: x[0])
len_sort_filt_numbers = len(sort_filt_numbers)

# 산술평균
len_numbers = len(numbers)
print(round(sum(numbers)/len_numbers))
# 중앙값
sort_numbers = sorted(numbers)
print(sort_numbers[round(len_numbers/2)])
# 최빈값
if len_sort_filt_numbers>=2:
    print(sort_filt_numbers[1][0])
else :
    print(sort_filt_numbers[0][0]) 
#범위
print(sort_numbers[len_numbers-1]-sort_numbers[0])


# 미로 만들기

N = int(input())
action = input()

loc = [(0,0)]
dx,dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상우하좌
status = 2 # 남쪽방향을 보고 서있음

for a in action:
    if a == "R": # 방향 전환
        status = (status + 1) %4
    elif a == "L": # 방향 전환
        status = (status -1) %4
    else : # 실질적 이동
        x = loc[-1][0]+ dx[status]  # 가장 최근값에 접근
        y = loc[-1][1]+ dy[status]
        loc.append((x,y))

# 미로를 만들어주기 위한 최대최소값 구하기
x_sort = sorted(loc, key=lambda x: x[0])
y_sort = sorted(loc, key=lambda x: x[1])
x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]

# 일단 벽으로 채워놓고, 지나간 길을 업데이트 하자
matrix = [['#'] * (x_max-x_min+1) for _ in range(y_max-y_min+1)]

for i, j in loc:
    matrix[i][j] = '.'

for row in matrix:
    print(''.join(row))
