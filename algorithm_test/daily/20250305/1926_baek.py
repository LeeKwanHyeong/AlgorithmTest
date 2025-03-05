import sys
from collections import deque
sys.stdin = open('1926_input.txt')
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

visited = [[False] * m for _ in range(n)]

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    size = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((ny, nx))
                size += 1

    return size

picture_count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            picture_count += 1
            max_size = max(max_size, bfs(i, j))

print(picture_count)
print(max_size)
