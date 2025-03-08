import sys
sys.stdin = open('inflearn_dfs_9_input.txt')
input = sys.stdin.readline
n, f = map(int, input().split())
p = [0] * n
b = [1] * n
ch = [0] * (n+1)

def dfs(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end= ' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                dfs(L+1, sum + p[L] * b[L])
                ch[i] = 0

for i in range(1, n):
    b[i] = b[i-1] * (n-i) / i

dfs(0, 0)