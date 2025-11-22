import sys
# 입력 속도 개선
A, B, V = map(int, sys.stdin.readline().split())

if V <= A:
    print(1)
else:
    target_distance = V - A 
    net_gain = A - B
    days_before_last = (target_distance + net_gain - 1) // net_gain
    print(days_before_last + 1)