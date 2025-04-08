import sys
sys.stdin = open('14501_input.txt')
input = sys.stdin.readline
N = int(input())
T, P = [], []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    print(i, T[i])
    if i + T[i] <= N:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])

