N = int(input())

l = [input()for _ in range(N)]

bucket = [[]for _ in range(51)]

for i in range(N):
    bucket[len(l[i])].append(l[i])

for i in range(51):
    if bucket[i] :
        set_data = set(bucket[i])
        bucket[i] = list(set_data)
        bucket[i].sort()
        print(*bucket[i],sep='\n')