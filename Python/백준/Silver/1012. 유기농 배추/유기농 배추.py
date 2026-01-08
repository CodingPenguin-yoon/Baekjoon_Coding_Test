import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def vegetable(x,y):

    if x < 0 or x >= M or y < 0 or y >= N:
        return False

    if k_map[y][x] == 1:
        k_map[y][x] = 0

        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            vegetable(nx, ny)
        return True

    return False

T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())
    k_map = [([0] * M) for _ in range(N)]
    sum_ans = 0

    for i in range(K):
        k_x, k_y = map(int, input().split())
        k_map[k_y][k_x] = 1

    for i in range(N):
        for j in range(M):

            if vegetable(j,i):
                sum_ans += 1

    print(sum_ans)
