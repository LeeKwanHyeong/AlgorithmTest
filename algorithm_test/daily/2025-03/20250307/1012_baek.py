import sys
from collections import deque
sys.stdin = open('1012_input.txt')
input = sys.stdin.readline



# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면
# 이 지렁이는 인접한 다른 배추로 이동 가능
# 상하좌우

dx, dy = (-1,0,1,0), (0, 1, 0, -1)

T = int(input())


def bfs(start_x, start_y, board, visited, n, m):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))


for _ in range(T):
    m, n, k = map(int, input().split()) # M: 가로, N: 세로, K 배추 위치
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    count = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j, board, visited, n, m)
                count += 1

    print(count)


