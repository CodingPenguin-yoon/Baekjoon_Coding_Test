array = [-1] * 26

S = input()

for i in range(len(S)):

    Seq = ord(S[i]) % 97

    if(array[Seq] == -1):
        array[Seq] = i

print(*array)