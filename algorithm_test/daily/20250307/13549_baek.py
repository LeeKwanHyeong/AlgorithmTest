import sys
from collections import deque

sys.stdin = open('13549_input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())


queue = deque([(n, 0)])
visited = [-1] * 100001
def bfs():
    while queue:
        x, time = queue.popleft()
        if x == k:
            return time

        if 0 <= 2*x <= 100000 and (visited[2*x] == -1 or visited[2*x] > time):
            visited[2*x] = time
            queue.appendleft((2*x, time))

        for nx in (2*x, x-1, x + 1):
            if 0 <= nx <= 100000 and (visited[nx] == -1 or visited[nx] > time + 1):
                visited[nx] = time + 1
                queue.append((nx, time + 1))

print(bfs())
