import sys
sys.stdin = open("input.txt", "r")


# 신용카드만들기

T = int(input())
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    Luhn = 0
    for n in range(1,len(numbers)+1):
        if n % 2 !=0 :
            Luhn += numbers[n-1]*2
        else :
            Luhn += numbers[n-1]
    if Luhn % 10 == 0:
        result = 0
    else :
        to10 = Luhn % 10
        result = 10-to10
    print(f"#{t} {result}")
    