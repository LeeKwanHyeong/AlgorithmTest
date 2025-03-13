import sys
from collections import deque
sys.stdin = open('2573_input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

def melt():
    melt_list = []

    for x in range(N):
        for y in range(M):
            if board[x][y] > 0:
                sea_count = sum(1 for i in range(4) if 0<=x+dx[i]<N and 0<=y+dx[i]<M and board[x+dx[i]][y+dy[i]] == 0)
                melt_list.append((x, y, sea_count))

    for x, y, sea in melt_list:
        board[x][y] = max(0, board[x][y] - sea)

def bfs(start_x, start_y, visited):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
def count_icebergs():
    visited = [[False] * M for _ in range(N)]
    iceberg_count = 0

    for x in range(N):
        for y in range(M):
            if board[x][y] > 0 and not visited[x][y]:
                iceberg_count += 1
                bfs(x, y, visited)
    return iceberg_count

year = 0

while True:
    melt()
    year += 1

    count = count_icebergs()
    if count >= 2:
        print(year)
        break

    if count == 0:
        print(0)
        break




