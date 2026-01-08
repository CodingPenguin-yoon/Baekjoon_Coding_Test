N = int(input())

n_map = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def slice(x,y,n):
    
    global blue
    global white

    color = n_map[y][x]

    for i in range(y,y+n):
        for j in range(x,x+n):
            if color != n_map[i][j]:
                m = n//2
                slice(x,y,m)
                slice(x + m, y,m)
                slice(x, y + m,m)
                slice(x + m, y + m,m)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
    return

slice(0,0,N)

print(white)
print(blue)