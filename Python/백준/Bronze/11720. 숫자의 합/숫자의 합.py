num_length = int(input())

num = input()
num_sum = 0
for i in range(num_length):
    num_sum = num_sum + int(num[i])

print(num_sum)