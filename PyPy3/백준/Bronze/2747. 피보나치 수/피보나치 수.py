n = int(input())
re1 = 1
re2 = 1
re3 = 0
re_list = [0,1,1,2,3]
if n < 5:
    print(re_list[n])
else:
    for i in range(2,n):
        re3 = re1 + re2
        re1 = re2
        re2 = re3
    print(re3)