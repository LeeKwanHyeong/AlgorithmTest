import sys
sys.stdin = open('11053_input.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    print(f'i = {i} (A[{i}] = {A[i]})')
    for j in range(i):
        if A[j] < A[i]:
            print(f'j = {j} (A[{j}] = {A[j]} -> OK) -> dp[{j}] = max({dp[i]}, {dp[j] + 1}) = {max(dp[i], dp[j] + 1)}')
            dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
    print()
print(max(dp))