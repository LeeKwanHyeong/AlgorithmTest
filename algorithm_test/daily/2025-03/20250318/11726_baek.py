import sys
sys.stdin = open('11726_input.txt')
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
dp[1] = 1
a, b = 1, 2

for i in range(3, N + 1):
    a, b = b, (a + b) % 10007

print(b if N > 1 else a)
