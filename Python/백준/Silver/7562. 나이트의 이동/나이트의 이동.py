from collections import deque

T = int(input())


dx = [2, 2, 1, 1, -1 ,-1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def bfs(x,y):

    if x == fin_x and y == fin_y:
        return 0

    queue = deque([(x, y)])

    while queue:

        nx, ny = queue.popleft()
        if nx == fin_x and ny == fin_y:
            return visited_map[ny][nx]

        for i in range(8):
            x = nx + dx[i]
            y = ny + dy[i]

            if 0 <= x < I and 0 <= y < I:
                if visited_map[y][x] == 0:
                    visited_map[y][x] = visited_map[ny][nx] + 1
                    queue.append((x, y))
    return None






for _ in range(T):
    I = int(input())

    visited_map = [[0] * I for _ in range(I)]

    start_x, start_y = map(int,input().split())

    fin_x, fin_y = map(int,input().split())

    print(bfs(start_x, start_y))






