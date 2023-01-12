# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

# test case
a,b = map(int,input().split())
diff_ab = a - b+1
print(diff_ab)