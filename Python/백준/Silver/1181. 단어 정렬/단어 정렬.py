# 최적화 

import sys

# 1. 속도: input 대신 sys.stdin.readline 사용
input = sys.stdin.readline

N = int(input())

# 3. 로직: 리스트 대신 set을 담아둠 (넣을 때 자동 중복 제거)
bucket = [set() for _ in range(51)]

for _ in range(N):
    word = input().strip() # readline은 줄바꿈(\n)이 포함되므로 strip() 필수
    # 2. 메모리: 리스트 'l' 없이 바로 버킷에 넣음
    bucket[len(word)].add(word) 

for i in range(1, 51): # 길이가 0인 단어는 없으니 1부터 시작
    if bucket[i]:
        # set은 순서가 없으므로 출력 전에 정렬
        # sorted()는 정렬된 리스트를 반환함
        print(*sorted(bucket[i]), sep='\n')