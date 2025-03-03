import sys
sys.stdin = open('inflearn_bfs_ext_4_input.txt')
input = sys.stdin.readline

n = int(input())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(n)]
res = []
cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            dfs(xx, yy)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

print(res)