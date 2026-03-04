N = int(input())
for _ in range(N):

    N_array = input()
    start = 0
    end = len(N_array) - 1
    flag = True

    while start < end:
        if N_array[start] == N_array[end]:
            start += 1
            end -= 1
        else:
            buf_N = N_array[start+1:end+1]
            if buf_N == buf_N[::-1]:
                print(1)
                flag = False
                break

            buf_N = N_array[start :end]
            if buf_N == buf_N[::-1]:
                print(1)
                flag = False
                break

            print(2)
            flag = False
            break
    if flag:
        print(0)