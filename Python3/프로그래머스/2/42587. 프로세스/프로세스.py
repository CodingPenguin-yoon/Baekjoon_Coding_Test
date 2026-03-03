from collections import deque

def solution(priorities, location):
    proc = deque()
    for i, k in enumerate(priorities):
        proc.append((k, i))
    
    answer = 0 
    
    while proc:
        buf_proc, buf_i = proc.popleft()
        if proc and buf_proc < max(p[0] for p in proc):
            proc.append((buf_proc, buf_i))
        else:
            answer += 1
            if buf_i == location:
                return answer