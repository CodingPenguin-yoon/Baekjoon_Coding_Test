def solution(array, commands):
    answer = []
    
    for i in commands:
        buf = []
        buf = array[i[0]-1:i[1]]
        buf.sort()
        answer.append(buf[i[2]-1])
        
        
        
    return answer