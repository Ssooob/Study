import sys
sys.stdin = open("input.txt", "r")

# 10818 최소, 최대
N = int(input())
numbers = list(map(int,input().split()))
print(min(numbers), max(numbers))


# 11720 숫자의 합
N = int(input())
numbers = list(map(int,input()))
print(sum(numbers))


# 2750 수 정렬하기
T = int(input())
numbers = []
for t in range(T) :
    num = int(input())
    numbers.append(num)
s_numbers = sorted(numbers)
for s in s_numbers :
    print(s)



# 2562 최댓값
numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)
max_val = max(numbers)
max_idx = numbers.index(max_val)
print(max_val)
print(max_idx+1)

