N = int(input())

l = [list(map(int, input().split())) for _ in range(N)]
C = 1
C_l = []
for i in range(N):
    for j in range(N):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            C += 1
    C_l.append(C)
    C = 1

print(*C_l)