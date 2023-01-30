# 기본 코드 
import sys
sys.stdin = open("input.txt", "r")


# 10101 삼각형 외우기

# tri = [0]*3
# for t in range(3):
#    tri[t] = int(input())

# if sum(tri) == 180 :
#     if len(set(tri)) == 1:
#         print("Equilateral")
#     elif len(set(tri)) == 2:
#         print("Isosceles")
#     elif len(set(tri)) == 3:
#         print("Scalene")

# else :
#     print("Error")


'''
# 2720 세탁소 사장 동혁
Q,D,N,P = 25, 10, 5, 1
T = int(input())
for t in range(T):
    charge = int(input())
    nQ = charge//Q 
    charge = charge%Q
    nD = charge//D 
    charge = charge%D 
    nN = charge//N 
    charge = charge%N
    nP = charge//P 
    charge = charge%P

    print(nQ, nD, nN, nP)

# 더 간단한 방법
T = int(input())
moneys = [25, 10, 5, 1]
count = [0] * 4

for i in range(T):
    C = int(input())
    
    # 반복되는 것은 최대한 묶어주기 
    for j in range(len(moneys)):
        count[j] = C // moneys[j]
        C = C % moneys[j]

    # join으로 묶어주기
    print(' '.join(map(str, count)))

n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i

'''

'''
# 1453 피시방 알바
N = int(input())
seat = list(map(int,input().split()))
seat100 = [0]*101
cnt = 0
for i in seat :
    if seat100[i] != 0 :
        cnt += 1
    else :
        seat100[i] += 1
print(cnt)

# 더 간단한 풀이
N=int(input())
seats=list(map(int, input().split()))
s=len(list(set(seats)))
print(N-s)
'''

'''
# 2161 카드 
num = int(input())
card = [i for i in range(1,num+1)]
remove = []
for _ in range(len(card)):
    a = card.pop(0)
    remove.append(a)
    if len(card)>=2:
        b = card.pop(0)
        card.append(b)
print(*remove)

'''
# 큐로 풀경우
from collections import deque
num = int(input())
card = deque([i for i in range(1,num+1)])
cards = deque(list(range(1,num+1)))
print(card)
print(cards)


'''
# 큐로 풀경우
from collections import deque

n = int(input())
cards = deque(list(range(1,n+1)))
res= []
while cards :
    card = cards.popleft()
    res.append(card)
    if cards :
        card = cards.popleft()
        cards.append(card)
print(*res)

# https://alpyrithm.tistory.com/164

'''

'''
# 10773 제로
T = int(input())
num_list = []
for t in range(T):
    num = int(input())
    if num == 0 :
        num_list.pop(len(num_list)-1) # pop()하면 마지막꺼
    else :
        num_list.append(num)
print(sum(num_list))

'''


# 9012 괄호
'''
import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    flag = 0
    ps = deque()
    inp = sys.stdin.readline().strip()
    for item in inp:
        if (item == '('):
            ps.append('(')
        else:
            try:
                ps.pop()
            except:
                flag = 1
                break
    if (len(ps) == 0 and (flag == 0)):
        print("YES")
    else:
        print("NO")
'''
'''
left_braket = []
string = input()
for braket in string :
    if braket == "(":
        left_braket.append(braket)

    elif braket == ")":
        # 조건 1. 남은 왼쪽 괄호가 없을 때 -> 길이가 없어 짝 못 찾은 경우
        # 조건 2. 남은 왼쪽 괄호가 있을 때 -> 짝 맞추어 지워지는 경우

        if len(left_braket) == 0:
            print("NO")
        else :
            left_braket.pop()
'''
    
