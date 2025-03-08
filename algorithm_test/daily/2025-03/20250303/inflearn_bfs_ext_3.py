import sys
from collections import deque
sys.stdin = open('inflearn_bfs_ext_3_input.txt')
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
dq = deque()
matrix = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]

dq.append((0, 0))
matrix[0][0] = 1

while dq:
    tmp = dq.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and matrix[x][y]==0:
            matrix[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            dq.append((x, y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])