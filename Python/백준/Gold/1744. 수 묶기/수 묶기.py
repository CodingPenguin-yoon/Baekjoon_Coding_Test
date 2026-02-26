N = int(input())

minus = []
plus = []
zero_cnt = 0
one_cnt = 0
for _ in range(N):
        buf = int(input())
        if buf < 0:
            minus.append(buf)
        elif buf > 1:
            plus.append(buf)
        elif buf == 0:
            zero_cnt += 1
        else:
            one_cnt += 1



N_sum = 0
plus.sort(reverse=True)
minus.sort()
buf = 0

if len(plus)%2:
    plus_buf = plus.pop()
    for i, n in enumerate(plus):
        if i % 2:
            N_sum += buf * n
            buf = 0
        else:
            buf = n
    N_sum += plus_buf
else:
    for i, n in enumerate(plus):
        if i % 2:
            N_sum += buf * n
            buf = 0
        else:
            buf = n
if len(minus) % 2:
    minus_buf = minus.pop()
    for i, n in enumerate(minus):
        if i % 2:
            N_sum += buf * n
            buf = 0
        else:
            buf = n
    if zero_cnt == 0:
        N_sum += minus_buf
else:
    for i, n in enumerate(minus):
        if i % 2:
            N_sum += buf * n
            buf = 0
        else:
            buf = n

print(N_sum+one_cnt)