R,C,T = map(int,input().split())

RC_map = [list(map(int, input().split())) for _ in range(R)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]

up = -1
down = 0
for j in range(R):
    for i in range(C):
        if RC_map[j][i] == -1 and up == -1:
            up = (i,j)
        elif RC_map[j][i] == -1 and up != -1:
            down = (i,j)



def bfs(i,j,addition):
    if RC_map[j][i] <= 0:
        return

    spread_amount = RC_map[j][i] // 5
    if spread_amount == 0:
        return
    cnt = 0
    if RC_map[j][i] > 0:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < C and 0 <= ny < R and RC_map[ny][nx] != -1:
                addition[ny][nx] += RC_map[j][i] // 5
                cnt += 1
        RC_map[j][i] -= cnt * spread_amount


def gong_up(r):
    # 1. 왼쪽 벽 (위에서 아래로 내려옴)
    # 0번 행부터 공기청정기 바로 위 행까지의 값을 한 칸씩 내림
    for i in range(r - 1, 0, -1):
        RC_map[i][0] = RC_map[i - 1][0]

    # 2. 천장 (오른쪽에서 왼쪽으로 밀려옴)
    for i in range(C - 1):
        RC_map[0][i] = RC_map[0][i + 1]

    # 3. 오른쪽 벽 (아래에서 위로 올라감)
    for i in range(r):
        RC_map[i][C - 1] = RC_map[i + 1][C - 1]

    # 4. 공기청정기 행 (공기청정기에서 오른쪽으로 바람 나감)
    for i in range(C - 1, 1, -1):
        RC_map[r][i] = RC_map[r][i - 1]

    RC_map[r][1] = 0  # 나가는 바람은 먼지 0

def gong_down(r):
    # 1. 왼쪽 벽: 아래에서 위로 당김
    for i in range(r + 1, R - 1):
        RC_map[i][0] = RC_map[i+1][0]
    # 2. 바닥: 오른쪽에서 왼쪽으로 당김
    for i in range(C - 1):
        RC_map[R-1][i] = RC_map[R-1][i+1]
    # 3. 오른쪽 벽: 위에서 아래로 당김
    for i in range(R - 1, r, -1):
        RC_map[i][C-1] = RC_map[i-1][C-1]
    # 4. 공기청정기 행: 왼쪽에서 오른쪽으로 당김
    for i in range(C - 1, 1, -1):
        RC_map[r][i] = RC_map[r][i-1]
    # 공기청정기 바로 옆은 깨끗한 공기(0)
    RC_map[r][1] = 0

def monzi():
    addition = [[0] * C for _ in range(R)]
    for j in range(R):
        for i in range(C):
            bfs(i,j,addition)

    for j in range(R):
        for i in range(C):
            RC_map[j][i] += addition[j][i]

def gonggi():
    gong_up(up[1])
    gong_down(down[1])


for _ in range(T):
    monzi()
    gonggi()

sum = 0
for j in range(R):
    for i in range(C):
        sum += RC_map[j][i]

print(sum+2)
