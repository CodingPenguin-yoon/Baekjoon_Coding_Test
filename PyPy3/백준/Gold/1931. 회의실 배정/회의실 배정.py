
import sys
input = sys.stdin.readline
N = int(input())

N_array = []
for _ in range(N):
    start, end = map(int,input().split())
    N_array.append((start,end))

N_array.sort(key=lambda x: (x[1],x[0]))

count = 0
start_time_check = 0
for i in N_array:
    if start_time_check <= i[0]:
        count += 1
        start_time_check = i[1]

print(count)