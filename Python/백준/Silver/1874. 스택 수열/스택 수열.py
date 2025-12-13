import sys

input = sys.stdin.readline

N = int(input())
num_array = []

for i in range(N):
    num_array.append(int(input()))
result_array = []
result_array_chk = []
count_num = 1
flag = True
for num in num_array:
    while count_num <= num:
        result_array.append(count_num)
        count_num += 1
        result_array_chk.append("+")
    if result_array[-1] == num:
        result_array.pop()
        result_array_chk.append("-")
    else:
        print("NO")
        flag = False
        break
if flag:
    for v in result_array_chk:
        print(v)


"""
최적화

import sys

# 입력 속도 가속
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
current = 1
possible = True

for _ in range(n):
    target = int(input())
    
    # 1. 입력받은 수(target)까지 스택에 push
    while current <= target:
        stack.append(current)
        answer.append('+')
        current += 1
        
    # 2. 스택의 top이 target과 일치하는지 확인
    if stack and stack[-1] == target:
        stack.pop()
        answer.append('-')
    else:
        # 불가능한 경우 (스택이 비었거나, top이 target과 다름)
        possible = False
        break

if possible:
    # [핵심 최적화] 반복 print 대신 한 번에 출력
    print('\n'.join(answer))
else:
    print("NO")
"""