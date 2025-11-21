L = int(input())
S = input()

#r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891
# a r i m
r, M = 31, 1234567891

# ㅈㅅ

hash_sum = 0

for i in range(L):
    hash_sum = hash_sum + ( ( ord(S[i] ) - ord('a') + 1) * ( r ** i ))

print(hash_sum%M)