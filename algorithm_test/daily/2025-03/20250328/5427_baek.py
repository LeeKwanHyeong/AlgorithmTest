import sys
from collections import deque
sys.stdin = open('5427_input.txt')

dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)

def bfs(w, h, board):
    fire_q = deque()
    sang_q = deque()
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fire_q.append((i, j))
            elif board[i][j] == '@':
                sang_q.append((i, j, 0))
                visited[i][j] = True

    while sang_q:
        for _ in range(len(fire_q)):
            y, x = fire_q.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == '.':
                    board[ny][nx] = '*'
                    fire_q.append((ny, nx))

        for _ in range(len(sang_q)):
            y, x, t = sang_q.popleft()
            if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                return t + 1

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == '.' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    sang_q.append((ny, nx, t + 1))

    return "IMPOSSIBLE"




T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    print(bfs(w, h, board))