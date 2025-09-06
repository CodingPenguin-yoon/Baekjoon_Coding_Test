"""
1. 로직
- 백트래킹
- 숫자변수와 동일한 chk 불린을 만드는게 key
- 시작부분을 함수 변수로

2. 러닝 타임
- N^M

3. 변수
res = []
chk = []
"""
from collections import deque

n, m = map(int, input().split())
res = deque()
chk = [False] * (n+1)

def back(a):
    s = a
    if len(res) == m:
        print(*res)
        return
    for i in range(s, n+1):
        if not chk[i]:
            chk[i] = True
            res.append(i)
            back(i+1)
            chk[i] = False
            res.pop()
back(1)