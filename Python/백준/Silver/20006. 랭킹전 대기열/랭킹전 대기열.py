p, m = map(int,input().split())
room = []
for _ in range(p):
    level, player = input().split()
    match = False
    for i in room:
        if len(i) == m:
            continue

        if  int(i[0][0]) - 10 <= int(level) <= int(i[0][0]) + 10:
            i.append((level,player))
            match = True
            break
        else:
            continue


    if not match:
        room.append([(level,player)])

for i in room:
    i.sort(key=lambda x:x[1])
    if len(i) == m:
        print("Started!")
    else:
        print("Waiting!")

    for a, b in i:
        print(a,b)

