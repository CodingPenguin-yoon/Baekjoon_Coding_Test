def solution(friends, gifts):
    num_friends = len(friends)
    # gift_data 초기화는 잘 하셨습니다.
    gift_data = [[0] * num_friends for _ in range(num_friends)]

    # 개선점 1: 이름으로 인덱스를 바로 찾기 위한 딕셔너리(맵) 추가
    # 기존 코드처럼 이중 for문으로 친구 이름을 찾으면 시간 초과가 날 수 있습니다.
    # 이 딕셔너리를 사용하면 O(1) 시간 복잡도로 매우 빠르게 찾을 수 있습니다.
    friend_map = {name: i for i, name in enumerate(friends)}

    # 선물 기록 처리 로직 (수정)
    for gift in gifts:
        giv_buf, take_buf = gift.split()
        # 맵을 이용해 인덱스를 바로 찾습니다.
        giver_idx = friend_map[giv_buf]
        receiver_idx = friend_map[take_buf]

        # 버그 수정: i가 j에게 선물을 주면 gift_data[i][j]만 증가해야 합니다.
        gift_data[giver_idx][receiver_idx] += 1

    # 선물 지수 계산 로직 (수정)
    # .sum(axis=...)는 NumPy/Pandas 문법입니다. 기본 리스트에서는 수동으로 계산해야 합니다.
    gift_0 = [0] * num_friends  # 받은 선물 (take)
    gift_1 = [0] * num_friends  # 준 선물 (give)

    for i in range(num_friends):
        # i가 준 선물 총합 = i행의 합
        gift_1[i] = sum(gift_data[i])
        # i가 받은 선물 총합 = i열의 합
        for j in range(num_friends):
            gift_0[i] += gift_data[j][i]

    # gift_indic 계산
    gift_indic = []
    for i in range(num_friends):
        # 버그 수정: 선물 지수는 (준 선물 - 받은 선물) 입니다.
        gift_indic.append(gift_1[i] - gift_0[i])

    # 다음 달 받을 선물 계산 로직 (이 부분은 원래 로직이 정확했습니다)
    gift_answer = [0] * num_friends
    for i in range(num_friends):
        for j in range(i + 1, num_friends):
            # 규칙 1: 주고받은 기록 비교
            if gift_data[i][j] > gift_data[j][i]:
                gift_answer[i] += 1
            elif gift_data[j][i] > gift_data[i][j]:
                gift_answer[j] += 1
            # 규칙 2: 기록이 같으면 선물 지수 비교
            else:
                if gift_indic[i] > gift_indic[j]:
                    gift_answer[i] += 1
                elif gift_indic[j] > gift_indic[i]:
                    gift_answer[j] += 1

    # 최종 결과 반환
    return max(gift_answer) if gift_answer else 0