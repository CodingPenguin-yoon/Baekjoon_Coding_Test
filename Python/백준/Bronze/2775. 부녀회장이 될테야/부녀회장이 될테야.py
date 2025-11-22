C= int(input())

for _ in range(C):
    k = int(input())
    n = int(input())
    A_map = [[0] * 15 for _ in range(15)]
    for i in range(n+1):
        A_map[0][i] = i
    for i in range(1,k+1):
        for j in range(1,n+1):
            if j == 1:
                A_map[i][j] = 1
            else:
                A_map[i][j] = A_map[i - 1][j] + A_map[i][j - 1]
    print(A_map[k][n])