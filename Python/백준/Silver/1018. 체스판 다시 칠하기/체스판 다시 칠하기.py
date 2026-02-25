N, M = map(int,input().split())

chess = [input() for _ in range(N)]
cnt_B = 0
cnt_W = 0

ans = []
for i in range(N-7):
    for j in range(M-7):

        cnt_B = 0
        cnt_W = 0

        for k in range(i,i+8):
            for l in range(j,j+8):

                if (k+l) % 2 == 0:
                    if chess[k][l] != 'B':
                        cnt_B += 1
                    if chess[k][l] != 'W':
                        cnt_W += 1
                else:
                    if chess[k][l] != 'W':
                        cnt_B += 1
                    if chess[k][l] != 'B':
                        cnt_W += 1

        ans.append(cnt_B)
        ans.append(cnt_W)

print(min(ans))