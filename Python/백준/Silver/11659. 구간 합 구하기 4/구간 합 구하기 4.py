"""
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N

"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

N_list = list(map(int, input().split()))

n_sum_list = [0]
temp = 0
for i in N_list:
    temp += i
    n_sum_list.append(temp)

for _ in range(M):
    s_num, e_num = map(int,input().split())
    print(n_sum_list[e_num]-n_sum_list[s_num-1])
