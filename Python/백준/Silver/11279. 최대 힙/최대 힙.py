import sys
import heapq # 1. heapq 모듈 임포트
input = sys.stdin.readline

N = int(input().strip())

N_array = []

for _ in range(N):
    X = int(input().strip())
    X *= -1
    if not X:
        if not N_array:
            print(0)
        else:
            print(-1*heapq.heappop(N_array))
    else:
        heapq.heappush(N_array, X)