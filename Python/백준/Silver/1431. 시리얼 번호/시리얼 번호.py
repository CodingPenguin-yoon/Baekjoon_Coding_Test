N = int(input())
N_array = []
for _ in range(N):
    alpha_word = " "
    s = input()
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
    

    N_array.append((s,len(s),sum))

N_array.sort(key = lambda x : (x[1],x[2],x[0]))

for i in N_array:
    print(i[0])




