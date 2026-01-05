N = input()

num_list = list(map(int,input().split()))

#선물 줄바꿈
num_list.sort()

ans_time = 0
ans = 0
for i in num_list:
    ans_time += i
    ans += ans_time


print(ans)
