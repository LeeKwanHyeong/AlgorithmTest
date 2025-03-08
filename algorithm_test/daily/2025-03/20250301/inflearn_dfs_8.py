import sys
sys.stdin = open('inflearn_dfs_8_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(L):
    global cnt, res
    if L == M:
        for j in range(L):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L+1)
                ch[i] = 0


res = [0] * N
ch = [0] * (N+1)
cnt = 0
dfs(0)
print(cnt)