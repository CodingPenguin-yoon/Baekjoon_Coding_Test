#2
#3 ABC
#5 /HTP
#나시고랭 ㅎㅎ;;
T = int(input())

for _ in range(T):
    N, S = input().split()
    N = int(N)
    for i in range(len(S)):
        print(S[i]*N, end = "")
    print()