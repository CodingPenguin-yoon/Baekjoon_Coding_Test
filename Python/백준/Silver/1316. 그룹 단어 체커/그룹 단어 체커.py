N = int(input())
count = 0
for _ in range(N):
    word_array = input()
    alpha_array = [False] * 26
    is_group_word = True
    paste_word = ''
    for i in word_array:
        if i != paste_word:
            if alpha_array[(ord(i) - 97)]:
                is_group_word = False
                break
            alpha_array[(ord(i) - 97)] = True
            paste_word = i
    if is_group_word:
        count += 1

print(count)
