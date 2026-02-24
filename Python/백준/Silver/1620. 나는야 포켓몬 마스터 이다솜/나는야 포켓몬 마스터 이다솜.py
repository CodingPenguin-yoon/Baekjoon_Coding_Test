
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
dic = {}
N_list = [" "]
for i in range(1,N+1):
    Poket = input().strip()
    dic[Poket] = i
    N_list.append(Poket)


for _ in range(M):
    P = input().strip()
    if P.isdigit():
        print(N_list[int(P)])
    else:
        print(dic[P])

