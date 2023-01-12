# 기본 코드
import sys
sys.stdin = open("input.txt", "r")


num = int(input())

for i in range(1,num+1):
    if num % i == 0 :
        print(i,end=" ")
