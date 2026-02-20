import sys


input = sys.stdin.readline
N, M = map(int,input().split())
word_count = 0
word_array = []
for _ in range(N):
    word_array.append(input())

word_set = set(word_array)
for _ in range(M):
    if input() in word_set:
        word_count += 1

print(word_count)