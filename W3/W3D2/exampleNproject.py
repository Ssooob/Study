# Example
'''
#1

number = int(input())
print(number)


#2
numbers = list(map(int,input().split()))
print(numbers)
# 공백으로 구분되어있는 애를 받아서 일괄적으로 정수화 한 다음, list로 저장


#3
string = input().split()
print(string)


#4
a,b = list(map(int,input().split()))
print(a,b)
print(type(a))


#5

T = int(input())

for t in range(1,T+1):
    print(t)

    # 입출력 코드
    pass
'''

# Project
'''
#1
number = input("정수를 출력하세요")
print(number)


#2
string = input(" 단어를 구분해서 출력하세요: ").split(" ")
print(string)


#3
T = int(input())
for t in range(1,T+1):
    print(t)

    # 입출력 코드
    pass


#6
string = input().split()
print(string)


#8 
T = int(input())

for t in range(1,T+1):
    numbers = list(map(int, input("입력하세요").split()))
    print(numbers)
'''
