
while 1:
    ans = []
    word = input()
    flag = False

    if word == ".":
        break

    for i in word:
        if i == '(':
            ans.append(i)
        elif i == '[':
            ans.append(i)
        elif i == ')':
            if ans:
                buf = ans.pop()
            else:
                flag = True
                break

            if buf == '(':
                continue
            else:
                flag = True
                break
        elif i == ']':
            if ans:
                buf = ans.pop()
            else:
                flag = True
                break

            if buf == '[':
                continue
            else:
                flag = True
                break
    if flag:
        print("no")
        continue
    if ans:
        print("no")
    else:
        print("yes")
