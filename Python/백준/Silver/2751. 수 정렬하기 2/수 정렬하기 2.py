import sys
input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    S.add(int(input()))

print(*sorted(S), sep='\n')