# S, P = map(int,input().split())
#
# N_array = input()
#
# dic_ans = {}
# word = ['A','C','G','T']
# word_chk = list(map(int,input().split()))
# chk = 0
# cnt = 0
# for i in word:
#     dic_ans[i] = 0
# for i in N_array[0:P]:
#     dic_ans[i] += 1
# for i,k in enumerate(dic_ans.values()):
#     if i == 0:
#         if k >= word_chk[i]:
#             chk += 1
#     elif i == 1:
#         if k >= word_chk[i]:
#             chk += 1
#     elif i == 2:
#         if k >= word_chk[i]:
#             chk += 1
#     else:
#         if k >= word_chk[i]:
#             chk += 1
# if chk == 4:
#     cnt += 1
# chk = 0
#
# for j,i in enumerate(N_array[P:]):
#
#     chk = 0
#     if N_array[j] == 'A':
#         dic_ans[N_array[j]] -= 1
#     elif N_array[j] == 'C':
#         dic_ans[N_array[j]] -= 1
#     elif N_array[j] == 'T':
#         dic_ans[N_array[j]] -= 1
#     else:
#         dic_ans[N_array[j]] -= 1
#
#     if i == 'A':
#         dic_ans[i] += 1
#     elif i == 'C':
#         dic_ans[i] += 1
#     elif i == 'T':
#         dic_ans[i] += 1
#     else:
#         dic_ans[i] += 1
#
#     for i, k in enumerate(dic_ans.values()):
#         if i == 0:
#             if k >= word_chk[i]:
#                 chk += 1
#         elif i == 1:
#             if k >= word_chk[i]:
#                 chk += 1
#         elif i == 2:
#             if k >= word_chk[i]:
#                 chk += 1
#         else:
#             if k >= word_chk[i]:
#                 chk += 1
#     if chk == 4:
#         cnt += 1
#
# print(cnt)
import sys

input = sys.stdin.readline

# 1. 입력 받기
S, P = map(int, input().split())
dna = input().strip()
# A, C, G, T 순서대로 필요한 개수
min_counts = list(map(int, input().split()))

# 2. 초기 세팅
current_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
word = ['A', 'C', 'G', 'T']
satisfied = 0
ans = 0

# 🔥 수정 1: 필요 개수가 0인 문자는 이미 조건을 만족했으므로 satisfied 미리 증가
for i in range(4):
    if min_counts[i] == 0:
        satisfied += 1

# 특정 문자가 추가/제거될 때 조건을 만족하는지 체크하는 함수
def add_char(c):
    global satisfied
    current_counts[c] += 1
    idx = word.index(c)
    if current_counts[c] == min_counts[idx]:
        satisfied += 1

def remove_char(c):
    global satisfied
    idx = word.index(c)
    if current_counts[c] == min_counts[idx]:
        satisfied -= 1
    current_counts[c] -= 1

# 3. 첫 번째 윈도우 처리
for i in range(P):
    add_char(dna[i])

if satisfied == 4:
    ans += 1

# 4. 슬라이딩 윈도우 시작
for i in range(P, S):
    # 🔥 수정 2: satisfied = 0 삭제 (상태 유지가 핵심)
    j = i - P  # 나가는 문자의 인덱스
    add_char(dna[i])  # 새로 들어오는 문자
    remove_char(dna[j])  # 나가는 문자

    if satisfied == 4:
        ans += 1

print(ans)