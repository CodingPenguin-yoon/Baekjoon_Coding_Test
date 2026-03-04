import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    P = input().strip()
    N = int(input())
    raw_data = input().strip()[1:-1]

    if raw_data:
        dq = deque(raw_data.split(','))
    else:
        dq = deque()

    is_reversed = False
    is_error = False

    for cmd in P:
        if cmd == 'R':
            is_reversed = not is_reversed
        elif cmd == 'D':
            if not dq:
                print("error")
                is_error = True
                break
            if is_reversed:
                dq.pop()
            else:
                dq.popleft()

    if not is_error:
        if is_reversed:
            dq.reverse()
        print(f"[{','.join(dq)}]")