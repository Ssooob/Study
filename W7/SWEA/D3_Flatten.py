import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline
import heapq


for t in range(1,11):
    dump_num = int(input())
    dump_list = list(map(int,input().split()))
    heapq.heapify(dump_list)
    for d in range(dump_num):
        # 최대값 구하기
        max_val = max(dump_list)
        max_idx = dump_list.index(max_val)
        # 최대값에서 1 빼기 
        dump_list[max_idx] = dump_list[max_idx] - 1

        # 최소힙
        heapq.heappush(dump_list,heapq.heappop(dump_list)+1)

    # 최대 - 최소 
    print(f'#{t} {max(dump_list)-heapq.heappop(dump_list)}')
