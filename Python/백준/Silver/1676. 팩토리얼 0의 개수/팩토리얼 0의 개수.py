
N = int(input())

sum = 1
for i in range(1,N+1):
    sum *= i

strN = str(sum)
C = 0
for i in range(len(strN)):
    if '0' == strN[len(strN)-i-1]:
        C += 1
    else:
        break

print(C)