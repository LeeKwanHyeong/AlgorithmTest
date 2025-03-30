import sys
sys.stdin = open('11055_input.txt')
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = seq[:]

for i in range(N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + seq[i])

print(max(dp))