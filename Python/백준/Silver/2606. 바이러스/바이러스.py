N = int(input())
M = int(input())

N_map = [([0]*(N+1)) for _ in range(N+1)]

for _ in range(M):
    num1, num2 = map(int,input().split())
    N_map[num1][num2] = 1
    N_map[num2][num1] = 1

visit_map = [0]*(N+1)

def dfs(n):

    visit_map[n] = 1

    for i in range(1,N+1):
        if N_map[n][i] == 1 and visit_map[i] == 0 :
            dfs(i)

dfs(1)
print(visit_map.count(1)-1)