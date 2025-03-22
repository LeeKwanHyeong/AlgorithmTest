import sys
from collections import deque
sys.stdin = open('7562_input.txt')
input = sys.stdin.readline

N = int(input())

def bfs(s_y, s_x, e_y, e_x, n):
    if s_y == e_y and s_x == e_x:
        return 0
    queue = deque()
    queue.append((s_y, s_x, 0))
    visited = [[False] * n for _ in range(n)]
    visited[s_y][s_x] = True

    while queue:
        y, x, cnt  = queue.popleft()

        for dy, dx in [(-1, 2), (1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]:
            ny = y + dy
            nx = x + dx

            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if ny == e_y and nx == e_x:
                    return cnt + 1

                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
    return -1

for _ in range(N):
    n = int(input())
    s_y, s_x = map(int, input().split())
    e_y, e_x = map(int, input().split())

    print(bfs(s_y, s_x, e_y, e_x, n))