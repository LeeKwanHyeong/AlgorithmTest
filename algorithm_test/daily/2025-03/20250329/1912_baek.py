import sys
sys.stdin = open('1912_input.txt')
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [0] * n
dp[0] = seq[0]
result = dp[0]

for i in range(1, n):
    dp[i] = max(seq[i], dp[i-1] + seq[i])
    result = max(result, dp[i])
print(result)

