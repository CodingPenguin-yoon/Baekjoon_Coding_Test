"""
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.
"""

N, M = map(int,input().split())

tree = list(map(int,input().split()))

tree_max = max(tree)

end_H = tree_max
start_H = 0
result = 0
while start_H <= end_H:

    mid = (end_H+start_H)//2

    if result == mid:
        break


    total = 0

    for i in tree:
        temp = i - mid
        if temp > 0:
            total += temp

    if total < M:
        #result = mid
        end_H = mid - 1
    else:
        result = mid
        start_H = mid + 1
    #print(result)

print(result)




