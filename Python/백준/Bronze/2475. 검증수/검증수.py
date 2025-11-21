numarray = list(map(int, input().split()))

numarray_length = len(numarray)
num_sum = 0
correct_answer = 0
for i in range(numarray_length):
    num_sum = num_sum + numarray[i]**2

correct_answer= num_sum%10

print(correct_answer)