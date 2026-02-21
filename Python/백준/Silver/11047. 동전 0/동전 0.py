N, K = map(int,input().split())
N_array = []
for _ in range(N):
    N_array.append(int(input()))

N_array.sort(reverse=True)
count = 0
for i in N_array:
    count += K // i
    K %= i
print(count)