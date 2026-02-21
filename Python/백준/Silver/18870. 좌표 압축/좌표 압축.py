N = int(input())

N_array = list(map(int,input().split()))

ans_array = []
for i,x in enumerate(N_array):
    ans_array.append((i,x))

ans_array.sort(key=lambda x: (x[1]))
idx = -1
result = []
past_idx = ' '
for i in ans_array:
    if i[1] == past_idx:
        result.append((idx,i[0],i[1]))
    else:
        idx += 1
        result.append((idx,i[0],i[1]))
        past_idx = i[1]
result.sort(key=lambda x: (x[1]))

for i in result:
    print(i[0], end=' ')







