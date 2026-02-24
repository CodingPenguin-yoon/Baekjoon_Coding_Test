import sys
input = sys.stdin.readline


N, M = map(int,input().split())

dic = {}

for _ in range(N):
    A, B = input().split()
    dic[A] = B

for _ in range(M):
    A = input().strip()
    print(dic[A])
    