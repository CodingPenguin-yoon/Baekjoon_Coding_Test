from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_que = deque(truck_weights)
    cnt = 0
    bridge = deque([0] * bridge_length)
    truck_weight = 0
    
    
    while bridge:
        cnt += 1
        exit_t = bridge.popleft()
        truck_weight -= exit_t
        
        if truck_que:
            if truck_que[0] + truck_weight <= weight:
                truck_buf = truck_que.popleft()
                bridge.append(truck_buf)
                truck_weight += truck_buf
            else:
                bridge.append(0)

    return cnt