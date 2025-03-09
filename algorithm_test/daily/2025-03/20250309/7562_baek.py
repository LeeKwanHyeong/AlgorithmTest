import sys
from collections import deque
sys.stdin = open('7562_input.txt')

input = sys.stdin.readline

directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
              (1, 2), (-1, 2), (1, -2), (-1, -2)]


def bfs(l, start_x, start_y, end_x, end_y):
    if start_x == end_x and start_y == end_y:
        return 0

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * l for _ in range(l)]
    visited[start_x][start_y] = True

    while queue:
        x, y, moves = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if nx == end_x and ny == end_y:
                    return moves + 1

                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1


t = int(input())

for _ in range(t):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    print(bfs(l, start_x, start_y, end_x, end_y))