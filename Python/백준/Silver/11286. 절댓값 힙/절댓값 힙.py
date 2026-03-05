import heapq
import sys

input = sys.stdin.readline
N = int(input().strip())

x_array = []
for _ in range(N):

    x = int(input().strip())

    if x == 0:
        if x_array:
            i, a = heapq.heappop(x_array)

            if a:
                print(i)
            else:
                print(-i)
        else:
            print(0)
    elif x < 0:
        heapq.heappush(x_array,(-x, 0))
    else:
        heapq.heappush(x_array, (x, 1))


