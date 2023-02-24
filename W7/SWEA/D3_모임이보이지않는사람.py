import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline


T = int(input())
for t in range(1,T+1):
    voca = input().rstrip()
    voca_aeiou = voca
    for v in range(len(voca)) :
        if voca[v] in 'aeiou':
            voca_aeiou = voca_aeiou.replace(voca[v],'')
    print(f'#{t} {voca_aeiou}')