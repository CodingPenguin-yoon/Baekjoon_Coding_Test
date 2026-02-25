import heapq

N, M = map(int,input().split())

N_list = list(map(int,input().split()))
heap = []

for i in N_list:
    heapq.heappush(heap, i)

for _ in range(M):
    buf1 = heapq.heappop(heap)
    buf2 = heapq.heappop(heap)
    buf = buf1 + buf2
    heapq.heappush(heap, buf)
    heapq.heappush(heap, buf)

print(sum(heap))



