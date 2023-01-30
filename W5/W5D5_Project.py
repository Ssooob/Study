# 기본 코드 
import sys
sys.stdin = open("input.txt", "r",encoding='UTF8') # ,encoding='UTF8'


# 10817 세 수
'''
numbers = list(map(int,input().split()))
numbers.remove(max(numbers))
numbers.remove(min(numbers))
print(numbers[0])
'''

# 200001 고무오리 디버깅

duck= []
problem = 0
while 1 :
    duck = input()
    if duck == "문제":
        problem +=1 
    elif duck == "고무오리":
        if problem >=1:
            problem-=1
        else :
            problem +=2
    if duck == "고무오리 디버깅 끝":
        break
if problem == 0:
    print("고무오리야 사랑해")
else :
    print("힝구")


'''
# 1269 대칭 차집합
a,b = map(int,input().split())
a_num = set(map(int,input().split()))
b_num = set(map(int,input().split()))

print(len(a_num-b_num)+len(b_num-a_num))

'''
# 3052 나머지
'''
numbers= []
for i in range (10):
    a = int(input())% 42
    numbers.append(a)
print(len(set(numbers)))
'''

# 1181 단어 정렬
'''
T = int(input())
voca =[]
for t in range(T):
    voca.append(input())
voca = set(voca)
voca = list(voca)
voca.sort()
voca.sort(key = len)
print(*voca, sep='\n')
'''



