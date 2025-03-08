import sys
sys.stdin = open('inflearn_dfs_11_input.txt')
input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = int(input())


def dfs(L, s, sum):
    global cnt
    if L == K:
        if sum % res == 0:
            cnt += 1
    else:
        for i in range(s, N):
            dfs(L + 1, i + 1, sum + a[i])


cnt = 0
dfs(0, 0, 0)
print(cnt)