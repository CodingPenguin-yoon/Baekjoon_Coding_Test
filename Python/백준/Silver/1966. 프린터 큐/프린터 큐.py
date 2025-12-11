from collections import deque
case_number = int(input())
flag = False
found_index = -1
for _ in range(case_number):
    N, M = map(int,input().split())
    arr = deque(enumerate(map(int, input().split())))
    result = []

    while 1 :
        max_value = max(x[1] for x in arr)
        if arr[0][1] == max_value:
            result.append(arr.popleft())
        else:
            temp = arr.popleft()
            arr.append(temp)
        if not arr:
            break
    
    for i, (num, val) in enumerate(result):
        if num == M:
            found_index = i
            break
    print(found_index+1)
    found_index = -1






