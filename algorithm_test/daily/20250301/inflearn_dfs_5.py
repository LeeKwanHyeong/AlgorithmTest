import sys
sys.stdin = open('inflearn_dfs_5_input.txt')

C, N = map(int, sys.stdin.readline().split())

a = [0] * N
res = -2147000000

def dfs(l, sum, tsum):
    global res
    global total

    if sum + (total - tsum) < res:
        return

    if sum > C:
        return

    if l == N:
        if sum > res:
            res = sum
    else:
        dfs(l + 1, sum + a[l], tsum + a[l])
        dfs(l+1, sum, tsum + a[l])


for i in range(N):
    a[i] = int(sys.stdin.readline())

total = sum(a)
dfs(0, 0, 0)
print(res)