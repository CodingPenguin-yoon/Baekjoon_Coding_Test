N = int(input())

A = list(map(int,input().split()))

M =int(input())

B = list(map(int,input().split()))


dic_A = dict.fromkeys(A,0)

for a in A :
    if a in dic_A:
        dic_A[a] += 1


for a in B:
    print(dic_A.get(a,0),end=' ')

