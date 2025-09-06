"""
1. 로직
- 백트래킹
- 숫자변수와 동일한 chk 불린을 만드는게 key

2. 러닝 타임
- N!  < 10

3. 변수
res = []
chk = []
"""
from collections import deque

n, m = map(int, input().split())
res = deque()
chk = [False] * (n+1)

def back():
    if len(res) == m:
        print(*res)
        return
    for i in range(1, n+1):
        if not chk[i]:
            chk[i] = True
            res.append(i)
            back()
            chk[i] = False
            res.pop()

back()

