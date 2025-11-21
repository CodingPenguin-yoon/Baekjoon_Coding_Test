T = int(input())
for _ in range(T):
    N, S = input().split()
    ans = ""
    N = int(N)
    for i in range(len(S)):
        ans = ans+ S[i]*N

    print(ans)