# N = int(input())
# 
# N_array = list(map(int,input().split()))
# 
# ans_array = []
# for i,x in enumerate(N_array):
#     ans_array.append((i,x))
# 
# ans_array.sort(key=lambda x: (x[1]))
# idx = -1
# result = []
# past_idx = ' '
# for i in ans_array:
#     if i[1] == past_idx:
#         result.append((idx,i[0],i[1]))
#     else:
#         idx += 1
#         result.append((idx,i[0],i[1]))
#         past_idx = i[1]
# result.sort(key=lambda x: (x[1]))
# 
# for i in result:
#     print(i[0], end=' ')
# 
import sys
input = sys.stdin.readline

n = int(input())
n_array = list(map(int, input().split()))

# 1. 중복 제거하고 정렬하기 (이 순서가 곧 '순위'가 됩니다)
sorted_array = sorted(list(set(n_array)))

# 2. 딕셔너리를 이용해 각 값에 순위(index) 매기기
# 예: {-10: 0, -9: 1, 2: 2, 4: 3}
rank_dict = {val: i for i, val in enumerate(sorted_array)}

# 3. 원래 배열을 돌면서 딕셔너리에서 순위를 찾아 출력하기
# 하나씩 print하는 것보다 join을 쓰는 게 훨씬 빠릅니다.
print(*(rank_dict[x] for x in n_array))