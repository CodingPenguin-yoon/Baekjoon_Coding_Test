
doc = input()
word = input()

idx = 0
count = 0
word_len = len(word)

while idx <= len(doc) - word_len:
    # 1. 단어를 찾은 경우
    if doc[idx : idx + word_len] == word:
        count += 1
        idx += word_len  # 단어 길이만큼 점프 (중복 방지)
    # 2. 단어를 못 찾은 경우
    else:
        idx += 1         # 한 칸만 옆으로 가서 다시 확인

print(count)
# 가장 깔끔한 해결책
# word_list = input()
# word = input()
#
# print(word_list.count(word))