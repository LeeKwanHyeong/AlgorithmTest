import sys
from collections import deque
sys.stdin = open('inflearn_bfs_ext_1_input.txt')

MAX = 10000
chk = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())
chk[n] = 1
dis[n] = 0
dq = deque()
dq.append(n)
while dq:
    now = dq.popleft()
    if now == m:
        break

    for next in(now-1, now+1, now+5):
        if 0 < next <= MAX:
            if chk[next] == 0:
                dq.append(next)
                chk[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])