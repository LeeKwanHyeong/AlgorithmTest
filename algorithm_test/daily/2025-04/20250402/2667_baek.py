import sys
from collections import deque
sys.stdin = open('2667_input.txt')
input = sys.stdin.readline

N = int(input())
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def bfs(i, j):
    queue = deque()
    count = 1
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and board[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True
                count += 1
    return count

area_count = 0
res = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            area_count += 1
            res.append(bfs(i, j))

print(area_count)
res.sort(reverse=False)
print(*res, sep='\n')
