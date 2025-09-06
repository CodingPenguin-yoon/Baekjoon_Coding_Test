"""
1. 아이디어

- 3장을 계속 더함

2. 시간 복잡도
- N!

3. 자료구조
- cd[]

"""

n, m = map(int, input().split())
cd = list(map(int,input().split()))
black_answer = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            
            current_sum = cd[i] + cd[j] + cd[k]
            
            if black_answer < current_sum <= m:
                black_answer = current_sum

print(black_answer)