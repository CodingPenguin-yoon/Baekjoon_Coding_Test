# # push_front X: 정수 X를 덱의 앞에 넣는다.
# # push_back X: 정수 X를 덱의 뒤에 넣는다.
# # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# # size: 덱에 들어있는 정수의 개수를 출력한다.
# # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#
# import sys
# input = sys.stdin.readline
# from collections import deque
# N = int(input())
# que = []
# que = deque(que)
#
# for _ in range(N):
#     s = input().strip()
#     if ' ' in s:
#         com, X = s.split()
#         if com == "push_front":
#             que.appendleft(X)
#         else:
#             que.append(X)
#     else:
#         if s == "pop_back":
#             if not que:
#                 print(-1)
#             else:
#                 print(que.pop())
#         elif s == "pop_front":
#             if not que:
#                 print(-1)
#             else:
#                 print(que.popleft())
#         elif s == "size":
#             print(len(que))
#         elif s == "empty":
#             if not que:
#                 print(1)
#             else:
#                 print(0)
#         elif s == "front":
#             if not que:
#                 print(-1)
#             else:
#                 print(que[0])
#         elif s == "back":
#             if not que:
#                 print(-1)
#             else:
#                 print(que[-1])

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    line = input().split()
    command = line[0]

    if command == "push_front":
        dq.appendleft(line[1])
    elif command == "push_back":
        dq.append(line[1])
    elif command == "pop_front":
        print(dq.popleft() if dq else -1)
    elif command == "pop_back":
        print(dq.pop() if dq else -1)
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        print(1 if not dq else 0)
    elif command == "front":
        print(dq[0] if dq else -1)
    elif command == "back":
        print(dq[-1] if dq else -1)