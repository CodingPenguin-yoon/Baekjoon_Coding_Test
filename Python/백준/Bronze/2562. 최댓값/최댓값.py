max_num, max_i = 0,0
for i in range(9):
    N = int(input())
    if N > max_num:
        max_num = N
        max_i = i+1
print(max_num)
print(max_i)