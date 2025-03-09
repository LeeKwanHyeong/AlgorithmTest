import sys
from collections import deque
sys.stdin = open('2583_input.txt')
input = sys.stdin.readline

# M: 세로, N: 가로
M, N, K = map(int, input().split())
board = [[0] * N for _ in range(M)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 직사각형 내부를 1로 채우기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    # 직사각형 내부를 1로 설정 (y축 기준으로 뒤집혀있음)
    for i in range(y1, y2):  # 세로 방향
        for j in range(x1, x2):  # 가로 방향
            board[i][j] = 1

def bfs(x, y):
    queue = deque([(x, y)])
    board[x][y] = 1  # 방문 표시
    area_size = 1  # 현재 영역 크기

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny))
                area_size += 1

    return area_size

area_count = 0
area_size = []

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            area_size.append(bfs(i, j))
            area_count += 1

print(area_count)
print(" ".join(map(str, sorted(area_size))))