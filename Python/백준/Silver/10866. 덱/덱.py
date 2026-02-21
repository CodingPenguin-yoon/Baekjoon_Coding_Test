# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
que = []
que = deque(que)

for _ in range(N):
    s = input().strip()
    if ' ' in s:
        com, X = s.split()
        if com == "push_front":
            que.appendleft(X)
        else:
            que.append(X)
    else:
        if s == "pop_back":
            if not que:
                print(-1)
            else:
                print(que.pop())
        elif s == "pop_front":
            if not que:
                print(-1)
            else:
                print(que.popleft())
        elif s == "size":
            print(len(que))
        elif s == "empty":
            if not que:
                print(1)
            else:
                print(0)
        elif s == "front":
            if not que:
                print(-1)
            else:
                print(que[0])
        elif s == "back":
            if not que:
                print(-1)
            else:
                print(que[-1])