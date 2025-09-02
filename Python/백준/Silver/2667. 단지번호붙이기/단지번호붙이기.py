"""
1. 아이디어
- n,m 변수를 받아서 2중 for 문으로 맵을 만든다 & 이때 불린으로 False 로 된 맵도 동시에 생성한다.
- 인자로 받아온 맵을 돌면 BFS 를 그대로 시행한다.

2. 시간 복잡도 및 변수 단위 설정

- BFS : O(V + E)
- V : 25 * 25
- E : 4* 25 * 25
- V + E : 5* 25 * 25 = 725 < 200,000,000 연산 가능 범위

3. 자료구조
- 전체 지도 : int [][]
- 불린 지도 : bool [][]
- BFS : list [] (Queue)

그림과 똑같은 문제 이건 쌀먹용

"""
import sys
input = sys.stdin.readline


n = int(input())
#sys.stdin.readline 사용시  input 을 사용하게 되면 \n 까지 가져와서 map(int,"\n") 실행 돠면서 오류가 발생
# 따라서 .strip 으로 양 끝단 공백이나 줄바꿈 문자를 모두 제거함
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

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
            if 0 <= ny < n and 0 <= nx < n:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    area += 1
                    q.append((ny,nx))
    return area

for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            num.append(BFS(i,j))

print(len(num))
num.sort()
for i in range(len(num)):
    print(num[i])