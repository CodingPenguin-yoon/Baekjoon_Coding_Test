N1,N2 = map(int,input().split())
B_N = N1 if N1>N2 else N2
DIV = 0
for i in range(1,B_N+1):
    if (N1 % i == 0) and (N2 % i == 0):
        DIV = i
print(DIV)
print(N1*N2//DIV)
      
      
      
# def get_gcd(a, b):
#     # 유클리드 호제법 (반복문 버전)
#     while b:
#         a, b = b, a % b
#     return a
# 
# N1, N2 = map(int, input().split())
# 
# DIV = get_gcd(N1, N2)
# LCM = (N1 * N2) // DIV
# 
# print(DIV)
# print(LCM)