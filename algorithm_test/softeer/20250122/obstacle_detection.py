import sys
from collections import deque

sys.stdin = open('softeer/20250122/input.txt', 'r')


N = int(input())
block = [list(map(int, input())) for _ in range(N)]
print(block)

region = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
region_id = 0

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def bfs(x, y, region_id):
    queue = deque([(x, y)])
    

