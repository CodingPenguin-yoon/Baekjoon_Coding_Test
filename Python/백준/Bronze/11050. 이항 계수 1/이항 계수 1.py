N,K = map(int,input().split())
N_F = 1
K_F = 1
R_K = N - K
if N-K < K:
    R_K = K
    K=N - K
for i in range(N,R_K,-1):
    N_F *= i
for i in range(1,K+1):
    K_F *= i
print(N_F//K_F)