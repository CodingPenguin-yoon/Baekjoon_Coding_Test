num_sum = int(input())

size = list(map(int,input().split()))

T,P = map(int,input().split())

ans_T,ans_P1,ans_P2 = 0,0,0

for i in range(len(size)):
    ans_T = ans_T + ((size[i]-1)//T + 1)

print(ans_T)
ans_P1 = num_sum // P
ans_P2 = num_sum % P
print(ans_P1,ans_P2)