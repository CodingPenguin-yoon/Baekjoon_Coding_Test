# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     truck_que = deque(truck_weights)
#     cnt = 0
#     bridge = deque([0] * bridge_length)
#     truck_weight = 0
    
    
#     while bridge:
#         cnt += 1
#         exit_t = bridge.popleft()
#         truck_weight -= exit_t
        
#         if truck_que:
#             if truck_que[0] + truck_weight <= weight:
#                 truck_buf = truck_que.popleft()
#                 bridge.append(truck_buf)
#                 truck_weight += truck_buf
#             else:
#                 bridge.append(0)

#     return cnt

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque()
    
    current_weight = 0
    time = 0
    
    while truck_weights or bridge:
        time += 1
        
        if bridge and bridge[0][1] == time:
            w, _ = bridge.popleft()
            current_weight -= w
            
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                w = truck_weights.popleft()
                current_weight += w
                bridge.append((w, time + bridge_length))
            else:
                if bridge:
                    time = bridge[0][1] - 1
                    
    return time