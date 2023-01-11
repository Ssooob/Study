
# Example

#1 정수 1개 입력 받기
number = int(input())
print(number)


#2 공백으로 구분된 여러개의 정수 입력 받기
numbers = list(map(int,input().split()))
print(numbers)


#3 공백으로 구분된 여러개의 단어 입력 받기
string = input().split()
print(string)


#4 공백으로 구분된 2개의 정수 입력 받기
a, b = list(map(int,input().split()))
print(a, b)


#5 테스트 케이스 수가 주어지는 입력 받기
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    print(t)
    # 이하 입력 코드
    pass


#6 입력 줄 수가 주어지는 입력 받기
N = int(input()) # 입력 줄 수
for _ in range(N):
    # 이하 입력 코드
    pass


#7 테스트 케이스와 입력 줄 수가 주어지는 입력 받기
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    
    for _ in range(N):
        # 이하 입력 코드
        pass


# Project
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")


#1
numbers = list(map(int,input().split()))
for i in numbers :
    print(i,end=" ")


#2
strings= input().split()
for i in strings :
    print(i,end = " ")


#3
# Test case 입력
T= int(input())
print(T)

for t in range(1,T+1) :
    N = int(input())
    print(N)
    for n in range(N):
        num = int(input())
        print(num)


#4
T= int(input("test case: "))
print(T)
for t in range(1,T+1) :
    N = int(input("case :"))
    print(N)
    for n in range(1,N+1) :
        num1, num2 = map(int,input().split())
        print(f"{num1} {num2}")


#5
T= int(input("test case: "))
print(T)
for t in range(1,T+1):
    N =int(input())
    print(N)
    for n in range(N):
        strings= input().split()
        print(*strings)


#6
T= int(input("test case: "))
print(T)
for t in range(1,T+1):
    N =int(input())
    print(N)
    for n in range(N) :
        numbers = list(map(int,input().split()))
        print(*numbers)


#7
T,N = map(int,(input("test case & input case: ").split()))
print(T,N)
for t in range(1,T+1):
    for n in range(N) : 
        num = int(input())
        print(num)


#8
T,N = map(int,(input("test case & input case: ").split()))
print(T,N)
for t in range(1,T+1):
    for n in range(N) : 
        num1,num2 = map(int,(input().split()))
        print(f"{num1} {num2}")


#9
T,N = map(int,(input("test case & input case: ").split()))
print(T,N)
for t in range(1,T+1):
    for n in range(N) : 
        numbers = list(map(int,(input().split())))
        print(*numbers)