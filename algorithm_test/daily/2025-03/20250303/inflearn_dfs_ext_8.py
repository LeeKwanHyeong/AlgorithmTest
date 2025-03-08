import sys
sys.stdin = open('inflearn_dfs_ext_8_input.txt')
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0 <= xx < n and 0 <= yy < n and chk[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                chk[xx][yy] = 1
                dfs(xx, yy)
                chk[xx][yy] = 0



n = int(input())
board = [[0] * n for _ in range(n)]
chk = [[0] * n for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
max = -2174000000
min = 2174000000
sx, sy = 0, 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max:
            max = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]
chk[sx][sy] = 1
cnt = 0
dfs(0, 0)

print(cnt)