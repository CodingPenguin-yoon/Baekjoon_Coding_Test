
N = int(input())
city_road = list(map(int,input().split()))
price_list = list(map(int,input().split()))

price_sum = 0
now_price = 0
for i in range(N):

    if not i:
        now_price = price_list[i]
    else:
        if now_price > price_list[i]:
            now_price = price_list[i]

    road_now = city_road
    if i == N-1:
        road_now = 0
    else:
        road_now = city_road[i]


    price_sum += now_price * road_now

print(price_sum)