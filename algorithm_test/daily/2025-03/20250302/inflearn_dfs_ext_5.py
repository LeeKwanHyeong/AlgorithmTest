import sys
sys.stdin = open('inflearn_dfs_ext_5_input.txt')
input = sys.stdin.readline

def dfs(L):
    global res

    if L == n:
        diff = max(money) - min(money)
        if diff < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = diff
    else:
        for i in range(3):
            money[i] += coin[L]
            dfs(L + 1)
            money[i] -= coin[L]

n = int(input())
coin = []
money = [0] * 3
res = 2147000000
for _ in range(n):
    coin.append(int(input()))

dfs(0)
print(res)
