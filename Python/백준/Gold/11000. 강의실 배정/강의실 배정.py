import sys
import heapq
input = sys.stdin.readline

N = int(input())
N_array = []
for _ in range(N):
    A, B = map(int,input().split())
    N_array.append((A,B))

N_array.sort()

classroom_end = []

heapq.heappush(classroom_end,N_array[0][1])


for i in range(1,N):
    if N_array[i][0] >= classroom_end[0]:
        heapq.heappop(classroom_end)
    heapq.heappush(classroom_end,N_array[i][1])



print(len(classroom_end))



