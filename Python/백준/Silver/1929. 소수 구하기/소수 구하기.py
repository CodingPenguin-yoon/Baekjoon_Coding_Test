M, N = map(int,input().split())

prime_list = []
C = True
for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            C = False
            break
    if C:
        prime_list.append(i)
    C = True
print(*prime_list, sep='\n')
