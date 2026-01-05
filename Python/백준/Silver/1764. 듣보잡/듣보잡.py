import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 입력 받을 때부터 .strip()으로 깔끔하게 넣기
member_array = set()
for _ in range(N):
    member_array.add(input().strip())

answer_array = [] # 결과는 순서가 중요하니 리스트로!

for _ in range(M):
    mem = input().strip() # 비교할 때도 깔끔하게
    if mem in member_array:
        answer_array.append(mem)

# 2. ★핵심★ 보통 문제는 '사전순 출력'을 원합니다. 정렬 필수!
answer_array.sort()

print(len(answer_array))
for i in answer_array:
    print(i)