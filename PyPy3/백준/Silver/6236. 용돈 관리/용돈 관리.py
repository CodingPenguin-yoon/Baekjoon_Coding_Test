import sys

input = sys.stdin.readline
N, M = map(int,input().split())
N_array = []

for _ in range(N):
    N_array.append(int(input().strip()))

start = max(N_array)
end = sum(N_array)
mid = 0
result = 0
while start <= end:
    cnt = 1
    mid = (start + end)//2
    current_money = mid

    for i in N_array:
        if current_money < i:
            cnt += 1
            current_money = mid
        current_money -= i


    if cnt > M:
        start = mid + 1

    else:
        result = mid
        end = mid - 1

print(result)