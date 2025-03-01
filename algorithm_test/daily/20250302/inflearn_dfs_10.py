import sys
sys.stdin = open('inflearn_dfs_10_input.txt')
input = sys.stdin.readline

def dfs(L, s):
    global cnt, res
    if L == m:
        for j in range(L):
            print(res[j], end = ' ')
        cnt += 1
        print()
    else:
        for i in range(s, n+1):
            res[L] = i
            dfs(L+1, i+1)


n, m = map(int, input().split())
res = [0] * (n+1)
cnt = 0
dfs(0, 1)
print(cnt)