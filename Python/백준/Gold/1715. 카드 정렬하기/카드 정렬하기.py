import heapq
import sys

input = sys.stdin.readline
N = int(input())

N_array = []
sum_N = 0

for _ in range(N):
    heapq.heappush(N_array, int(input().strip()))

while len(N_array) != 1:
    buf1 = heapq.heappop(N_array)
    buf2 = heapq.heappop(N_array)
    buf = buf1 + buf2
    sum_N += buf
    heapq.heappush(N_array, buf)

print(sum_N)