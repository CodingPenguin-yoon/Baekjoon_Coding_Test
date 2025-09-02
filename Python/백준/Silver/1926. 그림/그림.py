"""
1. 아이디어
- n,m 변수를 받아서 2중 for 문으로 맵을 만든다 & 이때 불린으로 False 로 된 맵도 동시에 생성한다.
- 인자로 받아온 맵을 돌면 BFS 를 그대로 시행한다.

2. 시간 복잡도 및 변수 단위 설정

- BFS : O(V + E)
- V : 500 * 500
- E : 4* 500 * 500
- V + E : 5* 500 * 500 = 1,250,000 < 200,000,000 연산 가능 범위

3. 자료구조
- 전체 지도 : int [][]
- 불린 지도 : bool [][]
- BFS : list [] (Queue)
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

num = []
# 2차원 좌표로 생각하면 됨 오른쪽 위 왼쪽 아래
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def BFS(y,x):
    area = 1
    q = []
    q.append((y,x))
    while q:
        qy,qx = q.pop(0)
        for i in range(4):
            ny = qy + dy[i]
            nx = qx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    area += 1
                    q.append((ny,nx))
    return area

for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            num.append(BFS(i,j))

print(len(num))
print(max(num) if num else 0)