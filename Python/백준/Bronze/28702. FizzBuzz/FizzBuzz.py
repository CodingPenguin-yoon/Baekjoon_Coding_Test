array = []
for _ in range(3):
    array.append(input())


for i in range(3):
    if array[i] == "Fizz":
        continue
    elif array[i] == "Buzz":
        continue
    elif array[i] == "FizzBuzz":
        continue
    else:
        if i == 0:
            ans = int(array[i]) +3
        elif i == 1:
            ans = int(array[i]) + 2
        else:
            ans = int(array[i]) + 1
        break


if ans % 3 ==0 and ans %5 == 0 :
    print("FizzBuzz")
elif ans %3 == 0:
    print("Fizz")
elif ans %5 == 0:
    print("Buzz")
else:
    print(ans)
