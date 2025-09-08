import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 세로 R, 가로 C 입력
R, C = map(int, input().split())
# 보드 정보 입력
board = [list(input().strip()) for _ in range(R)]

# 상, 하, 좌, 우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 결과값을 저장할 변수
max_moves = 0

# 방문한 알파벳을 기록할 배열 (A-Z)
# ord(알파벳) - ord('A')를 인덱스로 사용
visited_alphabets = [False] * 26

def dfs(x, y, count):
    """
    깊이 우선 탐색 함수
    x, y: 현재 위치
    count: 현재까지 이동한 칸의 수
    """
    global max_moves
    # 현재 이동 횟수로 최대값 갱신
    max_moves = max(max_moves, count)

    # 4가지 방향(상, 하, 좌, 우)으로 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 1. 보드 범위 안에 있는지 확인
        if 0 <= nx < R and 0 <= ny < C:
            # 2. 다음 위치의 알파벳을 아직 방문하지 않았는지 확인
            alphabet_index = ord(board[nx][ny]) - ord('A')
            if not visited_alphabets[alphabet_index]:
                # 플래그 설정: 다음 알파벳을 방문했다고 표시
                visited_alphabets[alphabet_index] = True
                # 재귀 호출로 다음 탐색 진행 (이동 횟수 + 1)
                dfs(nx, ny, count + 1)
                # 백트래킹: 탐색이 끝나면 다른 경로를 위해 방문 표시를 해제
                visited_alphabets[alphabet_index] = False

# 시작점 (0, 0) 처리
start_alpha_index = ord(board[0][0]) - ord('A')
visited_alphabets[start_alpha_index] = True
dfs(0, 0, 1)

# 최종 결과 출력
print(max_moves)