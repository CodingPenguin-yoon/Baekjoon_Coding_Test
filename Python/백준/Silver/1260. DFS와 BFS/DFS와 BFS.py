from collections import deque

import sys
input = sys.stdin.readline

# 1. 노드 개수 N, 간선 개수 M, 시작 노드 V 입력
N, M, V = map(int, input().split())

# 2. 빈 인접 리스트 만들기 (N+1개인 이유는 1번 노드부터 쓰기 위함)
graph = [[] for _ in range(N + 1)]
visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)
# 3. M개의 간선 정보를 입력받아 리스트 채우기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선이므로 양쪽 다 추가

# 4. 중요: 1260번은 "번호가 낮은 노드부터 방문"해야 하므로 정렬 필수!
for i in range(1, N + 1):
    graph[i].sort()

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)