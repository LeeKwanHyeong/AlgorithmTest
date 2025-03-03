import sys
sys.stdin = open('inflearn_dfs_ext_6_input.txt')
input = sys.stdin.readline

def dfs(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(res[j], end = ' ')
        print()

    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                dfs(L + 1, P+1)
            elif i >= 10 and code[L] == i // 10 and code[L+1] == i % 10:
                res[P] = i
                dfs(L + 2, P+1)


code = list(map(int, input()))
n = len(code)
code.insert(n, -1)
res = [0] * (n+3)
cnt = 0
dfs(0, 0)
print(cnt)