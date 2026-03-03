from collections import deque
def solution(arr):
    answer = []
    queue = deque(arr)
    buf = 0
    past = -1
    for _ in range(len(queue)):
        buf = queue.popleft()
        
        if past == buf:
            continue
        else:
            answer.append(buf)
            past = buf
    return answer