def solution(s):
    
    sum = 0
    
    for i in s:
        
        if i == "(":
            sum += 1
        else:
            sum -= 1
        
        if sum < 0:
            return False
    
    return sum == 0
