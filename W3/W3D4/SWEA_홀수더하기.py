# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

# test case
T = int(input())

for t in range(1,T+1):
    new_numbers = []
    numbers = list(map(int, input().split()))
    for i in numbers:
        if i%2 != 0 :
            new_numbers.append(i)
    sum_numbers = sum(new_numbers)
    print(f"#{t} {sum_numbers}")
    

    
# 