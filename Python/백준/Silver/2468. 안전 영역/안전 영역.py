from collections import deque

I = int(input())

# 괄호 위치 수정: list(map(...)) for _ in range(I)
rain_map = [list(map(int, input().split())) for _ in range(I)]
rain_map_buf = [[0]*I for _ in range(I)]
visited = [[False]*I for _ in range(I)]
# 최댓값 구하기
h_max = max(map(max, rain_map))

def bfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        nx, ny = queue.popleft()

        for i in range(4):

            next_x = nx + dx[i]
            next_y = ny + dy[i]

            if 0 <= next_x < I and 0 <= next_y < I:
                if not visited[next_y][next_x]:
                    if rain_map_buf[next_y][next_x]:
                        queue.append((next_x, next_y))
                        visited[next_y][next_x] = True
                    else:
                        visited[next_y][next_x] = True




    pass

ans = []

for i in range(0, h_max+1):
    rain_map_buf = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]
    cnt = 0

    for y in range(I):
        for x in range(I):
            rain_map_buf[y][x] = 1 if rain_map[y][x] >= i else 0


    for y in range(I):
        for x in range(I):
            if not visited[y][x]:
                if rain_map_buf[y][x]:
                    bfs(x, y)
                    cnt += 1


    ans.append(cnt)


print(max(ans))
