N = int(input())
T_list = list(map(int, input().split()))
T, P = map(int, input().split())
remain = 0
share = 0
sum = 0
for i in range(len(T_list)):
    remain = T_list[i] % T
    share = T_list[i] // T
    if remain == 0:
        sum += share
    else:
        sum += share+1

print(sum)
print(N//P,N%P)
