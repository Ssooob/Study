import sys
sys.stdin = open("input.txt", "r")


# 신용카드만들기

T = int(input())
for t in range(1,T+1):
    numbers = input()
    numbers = numbers.replace('-','') 
    # replace 문자열?? 이거 나중에 정리하기 실수한거 또 정리 변수 바꿔서 넣기

    if numbers[0] in '34569' and len(numbers) == 16:
       result = 1
    else :
        result = 0

    print(f"#{t} {result}")
    