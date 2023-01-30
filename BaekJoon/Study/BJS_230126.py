# 기본 코드 
import sys
sys.stdin = open("input.txt", "r")

'''
# 10448 유레카 이론 
gaus_list = [n*(n+1)//2 for n in range(1, 46)] # 45번째 1035
euraka = [0]*1001

for i in gaus_list :
    for j in gaus_list :
        for k in gaus_list :
            if i+j+k <=1000:
                euraka[i+j+k] = 1
T = int(input())
for _ in range(T):
    print(euraka[int(input())])

'''

# 10448 유레카 이론 
import sys
input = sys.stdin.readline

def find(n):
    for i in range(len(t)):
        for j in range(i,len(t)):
            for k in range(j,len(t)):
                if t[i]+t[j]+t[k] == n:
                    return 1
    return 0

t = [1]
for i in range(2,45):
    t.append(t[-1]+i)
    #print(t)
for _ in range(int(input())):
    n = int(input())
    print(find(n))