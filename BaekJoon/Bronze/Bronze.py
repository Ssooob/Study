# https://solved.ac/problems/level/2
# 백준 브론즈 4
# 일단 여기다 풀고 괜찮은 문제는 따로 빼서 정리

# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

'''
# 1264 모음의 개수

# 여러 줄 받을 때
while True :
    line = input("입력 :")
    # 코드 끝나는 조건 -> 얘가 있으면 코드가 아예 종료이기 때문에, 함수가 상단에 위치해야함
    if line == '#':
        break
    cnt =  0
    for i in line :
        if i in 'aeiouAEIOU' : # 이런식으로 묶어서 받아도 됨
            cnt +=1
    print(cnt)


# 2083 럭비 클럽

# 여러 자료형의 입력을 받을 때 

while True :
    name, age, weight = input().split()
    age = int(age)
    weight = int (weight)

    if '#' in name :
        break

    if age > 17 or weight >=80:
        print(f"{name} Senior")
    else :
        print(f"{name} Junior")



# 2439 별 찍기1

# 문자열도 연산이 가능
star = int(input())
for i in range (1,star+1):
    star_line = ' '* (star-i) +'*'* i
    print (star_line)



# 2440 별 찍기
s
star = int(input())
for i in range (star,0,-1):
    star_line = '*'* i
    print (star_line)



# 1152 단어의 개수
strings = input().split()
print(len(strings))


# 1085 직사각형에서 탈출

# 경계면으로만 가면되니까 기본 x,y값도 중요
x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))


# 4153 직각삼각형
while True :
    num = list(map(int,input().split()))
    if sum(num) == 0:
        break
    max_val = max(num)
    num.remove(max_val)
    if max_val*max_val == num[0]*num[0] + num[1]*num[1] :
         print('right')
    else :
        print('wrong')


# 1546 평균
N = int(input())
scores = list(map(int,input().split()))
M = max(scores)
new_score = []
for i in scores:
    new_score.append((i/M)*100)
avg_score = (sum(new_score))/N
print(avg_score)



# 2577 숫자의 개수
mul = 1
for i in range(3):
    num = int(input())
    mul *= num
mult = list(str(mul))
nums= [0]*10
for i in range(10):
    nums[i] = mult.count(str(i))
    print(nums[i])


#2562 최댓값
numbers = []
for i in range(9):
    numbers.append(int(input()))
 
print(max(numbers))
print(numbers.index(max(numbers))+1)

#2908 상수
a,b = input().split()
a = a[::-1]
b = b[::-1]
print(max(int(a),int(b)))


# 2920 음계
numbers = list(map(int,input().split()))
cnt = 0 
for i in range(0,len(numbers)-1) :
    if numbers[i]-numbers[i+1] == 1 :
        cnt += 1
    elif numbers[i]-numbers[i+1] == -1 :
        cnt -= 1
if cnt == -7 :
    print('ascending')
elif cnt == 7 :
    print('descending')
else :
    print('mixed')



#8958 ox 퀴즈
T = int(input())
for t in range(0,T): 
    ox = input()
    count, cont_count = 0,0
    for o in ox :
        if o == 'O':
            cont_count +=1
            count += cont_count
        elif o == 'X':
            cont_count = 0
    
    print(count)


# 3502 나머지
numbers= []
for i in range (10):
    a = int(input())% 42
    numbers.append(a)
print(len(set(numbers)))


# 2231 분해합
N = (int(input()))
result = 0 # 어차피 계산되는 값이 없으면 0 도출이니까
for i in range(1,N+1):
    nums = list(map(int,str(i))) # 각 요소를 분해하고 싶으면 str로 받고 다시 변환ㅌ
    A = sum(nums) + i
    if N == A :
        result=i
        break
print(result)


# 2292 벌집
# 1 6(2~7) 12(8~19) 18(20~37) 24(38~61)
# 1 2(+1) 8(+6) 20(+12) 38(+18)
# 
# 1 7(+6) 19(+12) 37(+18) 61(+24)
# 1 2(+1) 9(+7=6+1) 22(+13 = 12 +1 ) 41(+19 = 18+1) 66(+25 = 24+1)
# 1 3(+2) 11 25 45
# 1 4(+3) 13 29 50 

N = int(input())
beehouse = 1
cnt = 1
while N > beehouse :
    beehouse += 6*cnt
    cnt +=1
print(cnt)
'''