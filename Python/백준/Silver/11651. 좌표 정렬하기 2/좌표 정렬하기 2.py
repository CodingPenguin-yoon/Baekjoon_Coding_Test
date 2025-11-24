
N = int(input())
G_l = [list(map(int,input().split()))for _ in range(N)]

G_l.sort(key=lambda x: (x[1], x[0]))

[print(*p) for p in G_l]
