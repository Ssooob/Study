import sys
sys.stdin = open("input.txt", "r")


# 10039
avg_score = [40]*5
for i in range(5):
    score = int(input())
    if score >= 40:
        avg_score[i] = score
print(int((sum(avg_score))/5))


# 10871 X보다 작은 수
N,X = map(int, input().split())
num_list = list(map(int,input().split()))
for num in num_list :
    if num < X :
        print(num,end=' ')


# 2480 주사위 세개
num_list = list(map(int,input().split()))
num_list1 = list(set(num_list))
if len(num_list1) == 1 :
    own = int(num_list1[0])*1000 + 10000
elif len(num_list1) == 3 :
    own = max(num_list1)*100
else :
    for i in range(3):
        if num_list.count(num_list[i]) ==2 :
            num = int(num_list[i])
            break
    own = int(num)*100 + 1000
print(own)

# 다른 사람 풀이 구글링해보니 더 간단한 방법도 있음
d1, d2, d3 = map(int, input().split())

if d1 == d2 == d3:
    print(10000 + d1 * 1000)
elif d1 == d2 or d1 == d3 or d2 == d3:
    print(1000 + d1 * 100) if d1 == d3 else print(1000 + d2 * 100)
else:
    print(max(d1, d2, d3) * 100)

# 10886 0 = not cute / 1 = cute

T = int(input())
sum = 0
for t in range(T):
    # 0은 안귀여움, 1은 귀여움
    a = int(input())
    sum += a
if sum >=(T+1)/2: 
    print("Junhee is cute!")
else :
    print( "Junhee is not cute!")



# 2506 점수계산

T = int(input())
result = list(map(int,input().split()))
total_score,score = 0,0
for t in range(T):
    if result[t] == 1:
        score += 1
        total_score += score
    elif result[t] == 0:
        score = 0
print(total_score)


    