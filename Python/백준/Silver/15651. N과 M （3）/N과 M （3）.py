"""
1. 로직
- 백트래킹

2. 러닝 타임
- N^M  < 10

3. 변수
res = []
"""

from collections import deque

n, m = map(int, input().split())
res = deque()

def back():
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n+1):

        res.append(i)
        back()
        res.pop()


back()