import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for t in range(1,T+1):
    rect = list(map(int,input().split()))

    if rect[0] == rect[1] == rect[2] :
        result = rect[0]
    elif rect[0] == rect[1] :
        result = rect[2]
    elif  rect[1] == rect[2] :
        result = rect[0]
    elif rect[0] == rect[2] :
        result = rect[1]
    print(f"#{t} {result}")