"""
i + m , j + n < 50

50^2*64 = 125, 000

"""
m, n = map(int,input().split())


N_map = n - 7

M_map = m - 7

C_B = 0
C_W = 0


A_array = [input() for _ in range(m)]

A_ans = []

for i in range(0,M_map):
    for j in range(0,N_map):
        for m in range(8):
            for n in range(8):
                N_M = m + n

                if N_M % 2 == 0:
                    if A_array[m+i][n+j] != 'B':
                        C_B += 1
                    if A_array[m + i][n+j] != 'W':
                        C_W += 1
                else:
                    if A_array[m + i][n+j] != 'W':
                        C_B += 1
                    if A_array[m + i][n + j] != 'B':
                        C_W += 1

        A_ans.append(min(C_W,C_B))
        C_W, C_B = 0,0



print(min(A_ans))