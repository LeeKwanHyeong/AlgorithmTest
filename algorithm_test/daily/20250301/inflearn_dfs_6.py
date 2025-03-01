import sys
sys.stdin = open('inflearn_dfs_6_input.txt')
input = sys.stdin.readline

def dfs(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i
            dfs(L+1)


n, m = map(int, input().strip().split())
res = [0] * m
cnt = 0
dfs(0)
print(cnt)