import sys

sys.stdin = open('11724_input.txt')
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a-1][b-1] = adj[b-1][a-1] = 1

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)