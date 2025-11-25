
N , K = map(int,input().split())

A_N = list(range(1,N+1))

idx = 0
result = []
while A_N:

    idx = (idx + K - 1)%len(A_N)
    result.append(A_N.pop(idx))

print('<' + ', '.join(map(str, result)) + '>')



