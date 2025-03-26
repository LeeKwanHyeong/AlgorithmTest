import sys
from collections import deque
sys.stdin = open('1697_input.txt')

N, K = map(int, input().split())


def bfs():
    queue = deque([(N, 0)])
    visited = [False] * 100001
    visited[N] = True


    while queue:

        x, m = queue.popleft()

        if x == K:
            return m


        for step in (x -1, x + 1, 2*x):
            if 0 <= step <= 100000 and not visited[step]:
                visited[step] = True
                queue.append((step, m+1))

print(bfs())

