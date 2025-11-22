import sys

# 1. 입력 속도 개선
input = sys.stdin.readline

# N 입력 (최대 10,000,000)
n = int(input())

# 2. 메모리 최적화: 숫자를 담을 리스트 대신 '개수'를 담을 배열 생성
# 수는 10,000보다 작거나 같은 자연수이므로 10001 크기면 충분 (약 40KB 소모)
count_array = [0] * 10001

# 3. 데이터 입력 및 카운팅
for _ in range(n):
    # 숫자를 리스트에 append 하지 않고, 해당 숫자 인덱스의 값을 1 증가시킴
    target = int(input())
    count_array[target] += 1

# 4. 출력
# 0부터 10000까지 순회하며, 개수만큼 반복 출력
for i in range(10001):
    # 해당 숫자가 한 번이라도 등장했다면
    if count_array[i] != 0:
        # 등장한 횟수만큼 반복해서 출력
        for _ in range(count_array[i]):
            sys.stdout.write(str(i) + '\n')