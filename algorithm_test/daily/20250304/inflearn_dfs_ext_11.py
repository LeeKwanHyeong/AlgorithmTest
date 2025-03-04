import sys
sys.stdin = open('inflearn_dfs_ext_11_input.txt')
input = sys.stdin.readline

def dfs(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y - 1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            dfs(x, y - 1)
        elif y + 1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            dfs(x, y + 1)
        else:
            dfs(x-1, y)

board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0] * 10 for _ in range(10)]
for y in range(10):
    if board[9][y] == 2:
        dfs(9, y)