N = int(input())-1
C = 1

while True:
    if N <= 0:
        break
    # ㅈㅅ
    N -= 6*C
    C += 1

print(C)