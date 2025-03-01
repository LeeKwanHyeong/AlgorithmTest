import sys
sys.stdin = open('inflearn_dfs_4_input.txt')

def dfs(l, sum):
    if sum > total // 2:
        return
    if l == n:
        if sum == (total - sum):
            print('YES')
            sys.exit(0)
    else:
        dfs(l + 1, sum + a[l])
        dfs(l+1, sum)


n = int(sys.stdin.readline())
a = list(map(int, input().split()))
total = sum(a)
dfs(0, 0)
print('NO')