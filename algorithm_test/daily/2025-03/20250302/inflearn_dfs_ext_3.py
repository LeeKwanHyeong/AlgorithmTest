import sys
sys.stdin = open('inflearn_dfs_ext_3_input.txt')
input = sys.stdin.readline

def dfs(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        dfs(L+1, sum + G[L])
        dfs(L+1, sum - G[L])
        dfs(L+1, sum)

n = int(input())
G = list(map(int, input().split()))
s = sum(G)
res = set()
dfs(0, 0)
print(s - len(res))