from collections import Counter

def solution(participant, completion):

    answer = Counter(participant) - Counter(completion)

    return list(answer.keys())[0]

# def solution(participant, completion):
    
#     participant.sort()
#     completion.sort()
#     ans = ""
    
#     for i in reversed(completion):
#         if participant[-1] == i:
#             participant.pop()
#         else:
#             ans = participant[-1]
#             break
#     return ans
    