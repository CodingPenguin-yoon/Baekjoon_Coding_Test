"""
N = 500,000

"""

from collections import deque

N = int(input())
dq = deque(range(1, N + 1)) # 1부터 N까지 큐에 넣기

while len(dq) > 1: # 카드가 한 장 남을 때까지 반복
    dq.popleft()          # 1. 제일 위 카드 버리기
    dq.append(dq.popleft()) # 2. 그 다음 카드를 뽑아서 제일 아래로 옮기기

print(dq[0])