# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

# 2576 홀수
numbers = []
sum = 0
for t in range(7):
    num = int(input())
    if num % 2 != 0:
        sum += num
        numbers.append(num)
if sum == 0:
    print(-1)
else :    
    print(sum)
    print(min(numbers))


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


# 10822 더하기
string = list(map(int,input().split(',')))
print(sum(string))



# 2754 학점계산
score = list(input())
standard = {
    "A" : 4.0,
    "B" : 3.0,
    "C" : 2.0,
    "D" : 1.0,
    "F" : 0.0
}
if len(score) >= 2 :
    if score[1] == '+':
        print(standard[score[0]]+0.3)
    elif score[1] == '-':
        print(standard[score[0]]-0.3)
    else :
        print(standard[score[0]])
else :
    print(standard[score[0]])


# 그냥 입력하는 방법도 있음 (구글링)
dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
       'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
       'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
       'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
       'F':'0.0'}
grade = input()
print(dic[grade])




# 7785 회사에 있는 사람
n = int(input())
dic = {}

for _ in range(n):
    name, log = input().split()
    dic[name] = log
    if log == "leave":
        del dic[name]

d = sorted(dic.items(), reverse=True)
dic = dict(d)

for key in dic.keys():
    print(key)