import sys
from collections import deque
sys.stdin = open('1697_input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs():
    queue = deque([(n, 0)])
    visited = [False] * 100001
    visited[n] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time

        for nx in (x-1, x + 1, x * 2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))

print(bfs())

