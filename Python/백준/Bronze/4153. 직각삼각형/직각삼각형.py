while True:
    S1 = list(map(int, input().split()))
    if S1[0] == 0 and S1[1] == 0 and S1[2] == 0:
        break
    S2 = []
    for i in S1:
        S2.append(i ** 2)
    S2.sort()
    if S2[0] + S2[1] == S2[2]:
        print("right")
    else:
        print("wrong")