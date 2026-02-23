N, K = map(int,input().split())

N_array = list(map(int, input().split()))

prefix_sum = [0]
temp = 0
ans = []
for i in range(N):
    temp += N_array[i]
    prefix_sum.append(temp)

for i in range(N-K +1):
    if i + K > N:
        break
    ans.append(prefix_sum[i + K] - prefix_sum[i])

print(max(ans))