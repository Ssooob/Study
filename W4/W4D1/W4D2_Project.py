# 기본 코드
import sys
sys.stdin = open("input.txt", "r")


# 9085 더하기
T = int(input())
for t in range(T) :
    N = int(input())
    numbers = list(map(int,input().split()))
    print(sum(numbers))


# 10824
numbers = list(input().split())
num1 = int(numbers[0]+ numbers[1])
num2  = int(numbers[2]+numbers[3])
print(num1+num2)


# 3009 네번째 점
x,y = [],[]
for r in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1 :
        xx = i
    if y.count(y[i]) == 1 :
        yy = i
print(x[xx],y[yy])
    

# 10952 A+B - 5

while True :
    a,b = map(int,input().split()) 
    if a==0 & b== 0 :
        break
    print(a+b)
    


# 1110 더하기 사이클

num1 = input() # 0~99
num = num1 # num으로 변수를 설정
N = int(num1) # 비교를 위해 변하지 않아야는 값
cnt = 0
if N < 10 : # 한자리일 경우 0 추가
    num = '0'+num1
while True :
    num2 = int(num[0])+int(num[1]) # 2 + 6 = 8  # 6 + 8 = 14 
    num2 = str(num2)
    num3 = num[1]+ num2[len(num2)-1] # 68
    num = num3
    cnt += 1
    if int(num3) == N:
        break
print(cnt)