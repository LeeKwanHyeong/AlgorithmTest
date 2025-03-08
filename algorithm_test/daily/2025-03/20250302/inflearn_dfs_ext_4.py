import sys
sys.stdin = open('inflearn_dfs_ext_4_input.txt')
input = sys.stdin.readline
T = int(input())
k = int(input())
cv = list() # 동전 금액 리스트
cn = list() # 동전 개수 리스트
for i in range(k):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt = 0

def dfs(L, sum):
    global cnt
    if sum > T:
        return

    if L == k:
        if sum  == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            dfs(L + 1, sum + (cv[L] * i))


dfs(0, 0)
print(cnt)


