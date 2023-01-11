
#1 정수 1개 입력

number = int(input())
print(number)

#2 정수 여러개 입력
numbers = list(map(int,input().split()))
print(numbers)

#3 공백으로 구분된 여러개의 단어 입력 받기
string = input().split()
print(string)


#4 공백으로 구분된 2개의 정수 입력 받기
a,b = list(map(int,input().split()))
print(a,b)


# Project

# 1
number = int(input())
print(number)

#2
a,b = list(map(int,input().split()))
print(a,b)

#3
a,b,c = list(map(int,input().split()))
print(a,b,c)

numbers = a,b,c = list(map(int,input().split()))
print(numbers)

#4
string = input().split()
print(string)



