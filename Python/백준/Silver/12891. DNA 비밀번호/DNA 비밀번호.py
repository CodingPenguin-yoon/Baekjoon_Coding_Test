S, P = map(int,input().split())

N_array = input()

dic_ans = {}
word = ['A','C','G','T']
word_chk = list(map(int,input().split()))
chk = 0
cnt = 0
for i in word:
    dic_ans[i] = 0
for i in N_array[0:P]:
    dic_ans[i] += 1
for i,k in enumerate(dic_ans.values()):
    if i == 0:
        if k >= word_chk[i]:
            chk += 1
    elif i == 1:
        if k >= word_chk[i]:
            chk += 1
    elif i == 2:
        if k >= word_chk[i]:
            chk += 1
    else:
        if k >= word_chk[i]:
            chk += 1
if chk == 4:
    cnt += 1
chk = 0

for j,i in enumerate(N_array[P:]):

    chk = 0
    if N_array[j] == 'A':
        dic_ans[N_array[j]] -= 1
    elif N_array[j] == 'C':
        dic_ans[N_array[j]] -= 1
    elif N_array[j] == 'T':
        dic_ans[N_array[j]] -= 1
    else:
        dic_ans[N_array[j]] -= 1

    if i == 'A':
        dic_ans[i] += 1
    elif i == 'C':
        dic_ans[i] += 1
    elif i == 'T':
        dic_ans[i] += 1
    else:
        dic_ans[i] += 1

    for i, k in enumerate(dic_ans.values()):
        if i == 0:
            if k >= word_chk[i]:
                chk += 1
        elif i == 1:
            if k >= word_chk[i]:
                chk += 1
        elif i == 2:
            if k >= word_chk[i]:
                chk += 1
        else:
            if k >= word_chk[i]:
                chk += 1
    if chk == 4:
        cnt += 1

print(cnt)
