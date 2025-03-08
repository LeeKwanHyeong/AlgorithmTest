import sys

sys.stdin = open('inflearn_dfs_3_input.txt')

def dfs(v):
    if v ==  n+1:
        for i in range(1, n+1):
            if chk[i] == 1:
                print(i, end = " ")
        print()
    else:
        chk[v] = 1
        dfs(v+1)
        chk[v] = 0
        dfs(v+1)


n = int(sys.stdin.readline())
chk = [0]*(n+1)
dfs(1)