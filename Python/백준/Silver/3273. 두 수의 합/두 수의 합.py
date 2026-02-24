N = int(input())
N_array = list(map(int,input().split()))
X = int(input())

N_array.sort()

start_N =0
end_N = N - 1
buf = 0
cnt = 0
while start_N < end_N:

    buf = N_array[start_N] + N_array[end_N]

    if buf < X:
        start_N += 1
    elif buf > X:
        end_N -= 1
    else:
        cnt += 1
        start_N +=1
        end_N -= 1


print(cnt)