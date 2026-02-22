from collections import deque

import sys
input = sys.stdin.readline
# 1. 노드 개수 N, 간선 개수 M, 시작 노드 V 입력
N, M = map(int, input().split())
# 2. 빈 인접 리스트 만들기 (N+1개인 이유는 1번 노드부터 쓰기 위함)
graph = [[] for _ in range(N + 1)]
visited_bfs = [False] * (N+1)
count = 0
# 3. M개의 간선 정보를 입력받아 리스트 채우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선이므로 양쪽 다 추가

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(1,N+1):
    if not visited_bfs[i]:
        bfs(graph, i, visited_bfs)
        count += 1

print(count)



