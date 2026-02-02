while 1:
    num_list = list(map(int,input().split()))
    num_list.sort()
    if num_list[2] == 0:
        break
    if num_list[2]**2 == num_list[0]**2 + num_list[1]**2:
        print("right")
    else:
        print("wrong")
    