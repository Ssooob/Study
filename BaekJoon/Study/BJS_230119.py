# 기본 코드
import sys
sys.stdin = open("input.txt", "r")
#i_n = int(sys.stdin.readline())

# 11655 ROT13
sentence = input()
ord_str = ''
Up = [i for i in range(65,91)]
Down = [i for i in range(97,123)]
Upper = Up+Up
Downer = Down+Down

for s in sentence :
    # 대문자일 경우
    if 65 <= ord(s) <= 90 :
        ord_s = chr(Upper[(ord(s)-ord('A'))+13])

    # 소문자일경우 
    elif 97 <= ord(s) <= 122 :
        ord_s = chr(Downer[(ord(s)-ord('a'))+13])

    # 그 외 문자
    else :
        ord_s = s 
    ord_str += ord_s
print(ord_str)


# 민욱님 코드
import string as ss

s = input()
up = ss.ascii_uppercase
low = ss.ascii_lowercase
rot_up = up[13:] + up[:13]
rot_low = low[13:] + low[:13]

trans_up = str.maketrans(up,rot_up) # replace 대체 
trans_low = str.maketrans(low,rot_low)

s = s.translate(trans_up)
s = s.translate(trans_low)
print(s)

# 광배님 코드
# 11655 ROT13
S = input()
result = ''
for i in S:
    if i.islower(): # -97 + 13 = -84
        result += chr((ord(i)-84) % 26 + 97)
    elif i.isupper(): # -65 + 13 = -52
        result += chr((ord(i)-52) % 26 + 65)
    else:
        result += i
print(result)

# 수현님 코드

s = sys.stdin.readline()
ord_s = list(map(ord, s))

for i in range(len(ord_s)):
    if (64 < ord_s[i] < 91):
        ord_s[i] += 13
        if ord_s[i] > 90:
            ord_s[i] -= 26
    elif (96 < ord_s[i] < 123):
        ord_s[i] += 13
        if ord_s[i] > 122:
            ord_s[i] -= 26

chr_s = list(map(chr, ord_s))
print(''.join(chr_s))



# 2581 소수
a = int(input())
b = int(input())
sum= 0
idx = []
for num in range(a,b+1) :
    cnt = 0
    if num > 1 :
        for n in range(2,num) :
            if num % n == 0 :
                cnt +=1
        if cnt == 0:
            sum+=num
            idx.append(num)
if sum == 0 : 
    print(-1)
else :
    print(sum)
    print(idx[0])

# 현준님 코드
M = int(input())
N = int(input())
prime = []
for i in range(M,N+1):
    for j in range(2,i+1):
        if i == j :
            prime.append(i)
        if i%j == 0:
            break
if prime :
    print(sum(prime))
    print(min(prime))
else :
    print(-1)


# 5622 다이얼
 # default 2sec & +1 -> +1 sec
call = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
string = list(input())
sec = 0
for i in string :
    for j in call :
        if i in j : 
            dial = call.index(j) +3
            sec += dial
print(sec)

# 민욱님 코드
import string
al = string.ascii_uppercase
nums = '22233344455566677778889999'
tr = str.maketrans(al,nums)
s = input()
t = len(s)
s = s.translate(tr)
for i in s:
    t += int(i)
print(t)

# 2775 부녀회장이 될테야

T = int(input())
for t in range(T):
    k = int(input())  
    n = int(input())  
    home = [[(j+1) for j in range(n)] for i in range(k+1)]
   
    for i in range(1,k+1): # k-1 층에 대한 사람 (1층부터)
        for j in range(n): # 호수에 대한 사람 (1호부터)
            home[i][j] = sum(home[i-1][:j+1])
    print(home[k][n-1])


    #print(floor)
    # 0층 : 1명, 2명, 3명, 4명
    # 1층 : 1명, 3명, 6명, 10명 
    # 2층 : 1명, 4명, 10명, 20명
    # 3층 : 1명, 5명, 15명, 35명 


# 11653 소인수분해
N = int(input())
while N !=1 :
    for i in range(2,N+1): # 소인수 분해는 2부터 N까지
        if N%i == 0:
            print(i)
            N = N//i
            break

# 2846 오르막길
N = int(input())
road = list(map(int,input().split()))
total_distance = []
distance = 0
for r in range(N-1):
    if road[r]<road[r+1]:
        distance += road[r+1]-road[r]
    else :
        total_distance.append(distance)
        distance = 0
total_distance.append(distance) # 마지막값
print(max(total_distance))

