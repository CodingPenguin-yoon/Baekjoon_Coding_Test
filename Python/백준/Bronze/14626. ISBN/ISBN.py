C_num = input()

C_num = [n for n in C_num]

C = 0
sum = 0
for i in range(12):
    if C_num[i] == '*':
        C = i
    else:
        if i % 2 == 0:
            sum += int(C_num[i])
        else:
            sum += 3*int(C_num[i])

if C % 2 == 0 :
    for i in range(10):
        if ((sum+i+int(C_num[12]))%10) == 0:
            ans = i
            print(ans)
            break
else:
    for i in range(10):
        if ((sum+3*i+int(C_num[12]))%10) == 0 == 0:
            ans = i
            print(ans)
            break