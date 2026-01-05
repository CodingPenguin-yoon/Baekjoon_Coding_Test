
import sys
input = sys.stdin.readline

M = int(input())
s = set()

for _ in range(M):
    line = input().split()
    command = line[0]

    # 1. 숫자가 필요 없는 명령어 먼저 처리 (깔끔함 + 속도)
    if command == "all":
        s = set(range(1, 21)) # 반복문보다 통째로 대입하는 게 빠름
        continue
    elif command == "empty":
        s = set()
        continue

    # 2. 숫자가 필요한 명령어 처리
    # 여기서 int 변환을 해야 안전함
    N = int(line[1])

    if command == "add":
        s.add(N)
    elif command == "remove":
        s.discard(N)
    elif command == "check":
        print(1 if N in s else 0)
    elif command == "toggle":
        if N in s:
            s.discard(N)
        else:
            s.add(N)