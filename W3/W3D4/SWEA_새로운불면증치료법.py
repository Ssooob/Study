# 기본 코드
import sys
sys.stdin = open("input.txt", "r")

# test case
T = int(input())
for t in range(1,T+1): 
    num = int(input())
    num_list = [0]*10
    k= 1

    # print(num_list)
    while True :
        # 계속 돌리면서 k 가 증가하는 코드 
        num_vari = str(num * k)
        num_vari_list = list(map(int, num_vari))
        k = k + 1
        for i in range(0,10):
            if i in num_vari_list:
                num_list[i] = 1
        if 0 not in num_list :
            break 
    print(f"#{t} {num_vari}")



