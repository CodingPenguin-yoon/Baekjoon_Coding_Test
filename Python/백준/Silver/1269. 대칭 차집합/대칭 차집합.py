
A, B = map(int,input().split())

A_list = list(map(int,input().split()))

B_list = list(map(int,input().split()))


A_set = set(A_list)
B_set = set(B_list)

A_cnt = 0

B_cnt = 0

for i in A_list:
    if i in B_set:
        continue
    A_cnt += 1

for i in B_list:
    if i in A_set:
        continue
    B_cnt += 1

print(A_cnt+B_cnt)