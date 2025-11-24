N = int(input())
G_l = [list(map(int,input().split()))for _ in range(N)]
G_l.sort()
[print(*p) for p in G_l]