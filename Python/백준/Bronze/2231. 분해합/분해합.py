S = input()

num = max(1, int(S) - 9 * len(S))
ans = 0
for i in range(num,int(S)):
    number_str = str(i)
    result_array_int = [int(digit) for digit in number_str]
    ans_num = i + sum(result_array_int)
    if ans_num == int(S):
        ans = i
        break

if ans==0:
    print(0)
else:
    print(ans)
