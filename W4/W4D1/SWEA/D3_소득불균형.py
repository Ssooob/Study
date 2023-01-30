import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    AVG = int(sum(numbers)/N)
    cnt = 0  # ~ 보다 작은 값에 대한 출력 뭐 이런 함수 있을 것 같은데;
    for n in numbers:
        if n <= AVG :
            cnt +=1
    print(f"#{t} {cnt}")
