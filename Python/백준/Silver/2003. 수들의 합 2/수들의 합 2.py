N, M = map(int,input().split())

N_array = list(map(int,input().split()))


start_N = 0
end_N = 0
buf = 0
cnt = 0

while start_N < N:
    while buf < M and end_N < N:
        buf += N_array[end_N]
        end_N += 1

    if buf == M:
        cnt += 1

    buf -= N_array[start_N]
    start_N += 1

print(cnt)

