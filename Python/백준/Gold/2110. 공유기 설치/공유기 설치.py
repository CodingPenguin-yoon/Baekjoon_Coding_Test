import sys

input = sys.stdin.readline

N, M = map(int,input().split())

N_array = []

for _ in range(N):
    N_array.append(int(input()))

N_array.sort()

start = 0
end = N_array[-1]
mid = 0
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    last_install = N_array[0]
    for i in range(1,N):
        if N_array[i] - last_install >= mid:
            cnt += 1
            last_install = N_array[i]
            if cnt >= M:
                break

    if cnt < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)