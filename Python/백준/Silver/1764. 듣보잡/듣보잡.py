
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
list_N = []
ans_list = []
for i in range(1,N+1):
    list_N.append(input().strip())

set_N = set(list_N)

for _ in range(M):
    P = input().strip()
    if P in set_N:
        ans_list.append(P)

ans_list.sort()

print(len(ans_list))
for i in ans_list:
    print(i)
