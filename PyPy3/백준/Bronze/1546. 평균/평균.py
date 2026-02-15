N = int(input())
N_list = list(map(int,input().split()))

max_num = max(N_list)

average_num = (sum(N_list)*100) / (max_num*N)

print(average_num)