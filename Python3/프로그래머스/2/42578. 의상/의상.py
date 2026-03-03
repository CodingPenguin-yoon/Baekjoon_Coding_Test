def solution(clothes):
    cloth_set = {}
    answer = 1
    for i in clothes:
        if i[1] in cloth_set:
            cloth_set[i[1]] += 1
        else:
            cloth_set[i[1]] = 1
    
    for j in cloth_set.values():
        answer *= (j+1)
        
    if answer == 1:
        return 0
    else:
        return answer-1