from collections import deque

N, K = map(int,input().split())


N_point = [0]*100001

def bfs(x,y):

    queue = deque([x])
    while queue:

        point = queue.popleft()
        if point == y:

            return N_point[y]

        for next_pos in (point - 1, point + 1, 2 * point):
            if 0 <= next_pos <= 100000:  # 인덱스 범위 확인
                if not N_point[next_pos]:  # 아직 방문 안 했다면
                    if next_pos == x:
                        continue
                    N_point[next_pos] = N_point[point] + 1
                    queue.append(next_pos)


print(bfs(N, K))