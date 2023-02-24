import sys
sys.stdin = open("input.txt", "r") # ,encoding='UTF8'
input = sys.stdin.readline

# 1927 최소힙
import heapq
T = int(input())
numbers = []
heapq.heapify(numbers)
for t in range(T):
    num = int(input())
    if num > 0 :
        heapq.heappush(num)

    