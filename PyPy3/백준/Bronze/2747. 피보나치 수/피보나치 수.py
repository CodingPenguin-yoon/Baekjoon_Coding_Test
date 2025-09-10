n = int(input())
re1 = 1
re2 = 1
re3 = 0
re_list = [0,1,1]
if n <= 2:
    print(re_list[n])
else:
    for _ in range(n-2):
        re3 = re1 + re2
        re1 = re2
        re2 = re3
    print(re3)