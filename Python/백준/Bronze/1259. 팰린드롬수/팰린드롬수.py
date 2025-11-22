while True:

    F_drop = input()
    num_len = len(F_drop)
    flag = False

    if int(F_drop) == 0:
        break

    for i in range(num_len//2):
        if F_drop[i] != F_drop[(num_len-i-1)]:
            flag = True
            break

    if flag:
        print("no")
    else:
        print("yes")

# while True:
#     F_drop = input()
# 
#     # 1. 종료 조건
#     if F_drop == '0':
#         break
# 
#     # 2. 팰린드롬 검사 (최적화된 방식)
#     # 문자열 S와 S를 뒤집은 문자열 S[::-1]을 비교
#     if F_drop == F_drop[::-1]:
#         print("yes")
#     else:
#         print("no")