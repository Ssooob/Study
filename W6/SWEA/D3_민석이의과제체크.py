import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split()) # N: 수강생 수, K : 제출한 수강생 수
    K_list = list(map(int,input().split())) # 제출한 수강생 번호
    nonK_list = []

    for j in range(1,N+1):
        #print(j)
        if j not in K_list :
            nonK_list.append(j)
            #print(nonK_list)
    print("#",end ="")
    print(t,*nonK_list)
