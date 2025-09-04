from collections import deque

m,n = map(int,input().split())

#m: 가로 , n: 세로

map = [list(map(int,input().split()))  for _ in range(n)]

day = 0
q = deque()

# 이문제의 핵심은 이부분 day 변수의 존재 day 변수를 같이 넣어서 언제 이 말썽쟁이 토마토마토가 변했는지 체크

for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            q.append((j,i,day))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(q):
    nx=0
    ny=0
    x = 0
    y = 0
    day_buf=0
    x,y,day_buf = q.popleft()
    day_buf += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if map[ny][nx] == 0:
                map[ny][nx] = 1
                q.append((nx, ny, day_buf))
    return day_buf
endday=0

# q 안에 인자가 끝날때까지 
while q:
    endday = bfs(q)

endday -= 1

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            endday = -1
            break

print(endday)
