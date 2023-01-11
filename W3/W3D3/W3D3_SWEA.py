
# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

# 2047 신문 헤드라인
strings = input()
print(strings.upper())


# 2025 N줄덧셈
num = int(input())
numbers = 0 
for i in range(1,num+1):
    numbers +=i
    # print(numbers)
print(numbers)


# 1936 1대1 가위바위보

a,b = map(int,input().split())
if (a == 2 and b ==1) or (a == 1 and b ==3) or (a == 3 and b ==2) :
    print("A")
else :
    print("B")


# 2027 대각선 출력하기
for i in range(1,6) :
    for j in range(1,6) :
        if i == j :
            print('#',end = '')
        else : 
            print('+',end = '')
    print()


# 2058 자릿수 더하기
number = list(map(int,(input()))) # 최대 4자리
sum = sum(number)
print(sum)


# 2019 더블더블
num = int(input())
for i in range(0,num+1):
    result = 2**i
    print(result, end = " ")
