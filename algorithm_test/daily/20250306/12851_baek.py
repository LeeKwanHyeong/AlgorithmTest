import sys
from collections import deque
sys.stdin = open('12851_input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

if n==k:
    print(0)
    print(1)
    sys.exit()

MAX = 100000

visited = [-1] * (MAX + 1)
ways = [0] * (MAX + 1)

def bfs():
    queue = deque([n])
    visited[n] = 0
    ways[n] = 1

    while queue:
        x = queue.popleft()

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX:
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    ways[nx] = ways[x]
                    queue.append(nx)
                elif visited[nx] == visited[x] + 1:
                    ways[nx] += ways[x]

bfs()
print(visited[k])
print(ways[k])