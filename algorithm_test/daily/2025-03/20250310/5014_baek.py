import sys
from collections import deque
sys.stdin = open('5014_input.txt')
input = sys.stdin.readline

# F: 전체 층, S: 강호가 지금 있는 층, G: 스타트링크가 있는 층
# U: 위로 U번 가는 버튼 D: 아래로 D번 가는 버튼
F, S, G, U, D = map(int, input().split())

elv = [0] * F
queue = deque([(S, 0)])
visited = [False] * (F+1)
visited[S] = True



def bfs():
    while queue:
        x, t = queue.popleft()
        if x == G:
            return t
        else:
            for i in (U, -D):
                nx = x + i
                if 1 <= nx <= F and not visited[nx]:
                    visited[nx] = True
                    queue.append((nx, t+1))
    return 'use the stairs'

print(bfs())