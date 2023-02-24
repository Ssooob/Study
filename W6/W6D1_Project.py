# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

#1225 이상한 곱셈
a,b = input().split()
a = list(map(int,a))
b = list(map(int,b))
print(sum(a)*sum(b))

#2438 별찍기 -1 
T = int(input())
for t in range(1,T+1):
    print('*'*t)

#2739 구구단
T = int(input())
for t in range(1,10):
    print(f'{T} * {t} = {T*t}')

#2953 나는 요리사다
score = [0]*5
for i in range(5):
    score[i] = sum(list(map(int, input().split())))
print(score.index(max(score))+1, max(score))


#2669 직사각형 네개의 합집합의 면적 구하기 

matrix = [[0]*100 for _ in range(100)]

for _ in range(4):
    squa = list(map(int,input().split()))
    for x in range(squa[0],squa[2]) :
        for y in range(squa[1],squa[3]):
            matrix[x][y] = 1

sum_m = 0
for i in range(100):
    sum_m+= sum(matrix[i])
print(sum_m)

# True & False로 하고, False 일때만 넓이 +1 -> 이러면 for문 한 번만 써도 됨

