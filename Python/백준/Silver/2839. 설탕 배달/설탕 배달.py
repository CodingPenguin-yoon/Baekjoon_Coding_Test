N = int(input())

C_5 = N // 5

for i in range( C_5 , -1 , -1 ):
    DIV5 = N - (5*i)
    DIV3 = DIV5 % 3
    if DIV3 == 0:
        print(i+(DIV5//3))
        break
else:
    print(-1)