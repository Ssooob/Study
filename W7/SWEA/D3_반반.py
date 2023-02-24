import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    sentence = input().rstrip()
    alpha = [0]*26
    for s in sentence :
        alpha[ord(s)-ord('A')] += 1

    if alpha.count(2) == 2 :
        result = 'Yes'
    else :
        result = 'No'
        
    print(f'#{t} {result}')