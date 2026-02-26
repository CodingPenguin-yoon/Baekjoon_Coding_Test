from collections import deque

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))

N_list.sort(reverse=True)
N_list = deque(N_list)

sum_Nlist = 0
cnt = 0
last_sum = 0

for i in N_list:
    cnt += 1
    sum_Nlist = cnt * i
    if last_sum < sum_Nlist:
        last_sum = sum_Nlist


print(last_sum)
