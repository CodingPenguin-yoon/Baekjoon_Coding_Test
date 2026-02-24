T = int(input())

for _ in range(T):
    dic = {}
    B_list = []
    result = 1
    N = int(input())

    for _ in range(N):
        _, B = input().split()
        if B in dic:
            dic[B] += 1
        else:
            dic[B] = 2


    B_list = list(dic.values())

    for i in B_list:
        result *= i
    print(result - 1)







