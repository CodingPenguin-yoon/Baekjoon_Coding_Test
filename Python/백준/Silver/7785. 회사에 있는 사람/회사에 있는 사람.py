import sys
input = sys.stdin.readline

T = int(input())
dic = {}
for _ in range(T):
    A, B = input().split()

    if B == "enter":
        dic[A] = 1
    else:
        dic.pop(A,None)

key_list = list(dic.keys())
key_list.sort(reverse=True)
for i in key_list:
    print(i)

