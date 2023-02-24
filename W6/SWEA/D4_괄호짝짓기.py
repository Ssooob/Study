# 기본 코드 
import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = 10
for t in range(1,T+1):
    N = int(input())
    breaket = list(input())
    a,b,c,d = 0,0,0,0
    for n in breaket:
        #print(n)
        if n == '(' :
            a+=1
        elif n == '[':
            b+=1
        elif n == '{':
            c+=1
        elif n == '<':
            d+=1
        elif n == ')':
            a-=1
        elif n == ']':
            b-=1
        elif n == '}':
            c-=1
        elif n == '>':
            d-= 1
    if a==0 and b == 0 and c == 0 and d == 0:
        print(f"#{t} {1}")
    else :
        print(f"#{t} {0}")
        
           


