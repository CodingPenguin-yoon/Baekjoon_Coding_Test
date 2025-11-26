import sys,os
input = sys.stdin.readline

K = int(input())
K_list = []
for i in range(K):
    
    clean_code = int(input())
    
    if clean_code == 0:
        K_list.pop()
    else:
        K_list.append(clean_code)

print(sum(K_list))