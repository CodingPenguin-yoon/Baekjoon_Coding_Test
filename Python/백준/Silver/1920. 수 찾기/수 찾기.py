# #첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다. 10,000,000,000
#
# N = int(input())
#
# num_array = list(map(int,input().split()))
#
# M = int(input())
#
# check_array = list(map(int,input().split()))
#
#
# num_max = max(num_array)
#
# num_array_sort = [0]*(num_max+1)
#
# for i in num_array:
#     num_array_sort[i] = 1
#
# for i in check_array:
#     try:
#         if num_array_sort[i] == 1:
#             print(1)
#         else:
#             print(0)
#     except:
#         print(0)
#         continue


N = int(input())
#
num_array = list(map(int,input().split()))
#
M = int(input())
#
check_array = list(map(int,input().split()))

num_set = set(num_array)

for i in check_array:
    if i in num_set:
        print(1)
    else:
        print(0)
