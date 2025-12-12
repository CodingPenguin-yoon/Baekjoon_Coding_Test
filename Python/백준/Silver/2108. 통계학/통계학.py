import sys

input = sys.stdin.readline

N = int(input())
temp = []
check_num = [0]*8001
for _ in range(N):
    num = int(input())
    temp.append(num)
    check_num[4000 + num] += 1

temp.sort()

print(int(round(sum(temp)/N)))
print(temp[N//2])

max_num = max(check_num)

if check_num.count(max_num) == 1:
    first_idx = check_num.index(max_num)
    print(first_idx - 4000)
else:
    first_idx = check_num.index(max_num)
    second_idx = check_num.index(max_num, first_idx + 1)
    print(second_idx - 4000)

print(temp[N-1]-temp[0])

