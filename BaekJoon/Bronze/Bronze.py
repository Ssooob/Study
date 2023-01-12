# https://solved.ac/problems/level/2
# 백준 브론즈 4
# 일단 여기다 풀고 괜찮은 문제는 따로 빼서 정리

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

star = int(input())
for i in range (star,0,-1):
    star_line = '*'* i
    print (star_line)

'''