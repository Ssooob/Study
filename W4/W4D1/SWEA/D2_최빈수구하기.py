import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N = int(input())
    score = [0]*101
    numbers = list(map(int,input().split()))
    for n in numbers :
        score[n]+=1
    max_idx = []
    for i in range(len(score)) :
        #print(max(score))
        if score[i] == max(score):
            max_idx.append(i)
    print(f"#{t} {max(max_idx)}")
