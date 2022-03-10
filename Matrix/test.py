

n, m = map(int, input().split())
map_m = [[0] * m for _ in range(n)]
x, y, direct = map(int, input().split())
map_m[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_l():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3


turn_c = 0
count = 1

while True:
    turn_l()

    nx = x + dx[direct]
    ny = y + dy[direct]
    if map_m[nx][ny] == 0 and array[nx][ny] == 0:
        map_m[nx][ny] = 1
        x = nx
        y = ny
        turn_c = 0

        count += 1
        continue
    else:
        turn_c += 1

    if turn_c == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]
        if array[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_c = 0

print(count)
