import sys
from collections import deque
sys.stdin = open('2667_input.txt')
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

area_sum = 0
area_size = []

def bfs(i, j):
    visited[i][j] = True
    queue = deque([(i, j)])
    area_count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<N and 0<=ny<N and board[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                area_count += 1

    return area_count

for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and not visited[i][j]:
            area_size.append(bfs(i, j))
            area_sum += 1

print(area_sum)
area_size.sort(reverse = False)
print(*area_size, sep='\n')
