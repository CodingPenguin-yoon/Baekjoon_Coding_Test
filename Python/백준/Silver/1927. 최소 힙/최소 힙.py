import sys
from collections import deque
import heapq

input = sys.stdin.readline

N = int(input())

num_list = []


for _ in range(N):
    num = int(input())
    if num == 0:

        if len(num_list) == 0:
            print(0)
        else:
            print(heapq.heappop(num_list))

    else:
        heapq.heappush(num_list,num)


