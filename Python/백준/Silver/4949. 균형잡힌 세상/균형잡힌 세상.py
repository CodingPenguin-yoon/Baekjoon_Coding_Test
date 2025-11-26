while True:
    ans = []
    n = input()
    if n == '.':
        break
    for i in range(len(n)):
        if n[i] == '(':
            ans.append('(')
        if n[i] == ')':
            if len(ans) == 0:
                print("no")
                break
            C_A = ans.pop()
            if C_A !='(':
                print("no")
                break
        if n[i] == '[':
            ans.append('[')
        if n[i] == ']':
            if len(ans) == 0:
                print("no")
                break
            C_A = ans.pop()
            if C_A != '[':
                print("no")
                break
    else:
        if len(ans) == 0:
            print("yes")
        else:
            print("no")