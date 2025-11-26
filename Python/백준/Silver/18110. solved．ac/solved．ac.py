import  sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))

    n_list.sort()

    # [수정 1] 절사 평균 인원 구하기 (파이썬 round 대신 수동 반올림)
    m = int(n * 0.15 + 0.5)

    low_sum = 0
    high_sum = 0

    # 파는 치던 대로 계속 칩니다 (슬라이싱 없이 for문 유지)
    for i in range(m):
        low_sum += n_list[i]
        high_sum += n_list[n-1-i]

    # [수정 2] 최종 평균 구하기 (여기도 수동 반올림)
    # 전체 합에서 위아래 합을 빼고 나눔
    final_score = (sum(n_list) - low_sum - high_sum) / (n - 2 * m)
    print(int(final_score + 0.5))