import sys
sys.stdin = open('1932_input.txt')
input = sys.stdin.readline

N = int(input())
dp = [[0] * N for _ in range(N)]
triangle = [list(map(int, input().split())) for _ in range(N)]

dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        print(i, j)
        if j == 0: # 왼쪽 끝
            dp[i][j] = dp[i-1][j] + triangle[i][j]
            print(dp[i-1][j], triangle[i][j])
        elif j == i: # 오른쪽 끝
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            print(dp[i-1][j-1], triangle[i][j])
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            print(dp[i-1][j-1], dp[i-1][j], triangle[i][j])

        for k in dp:
            print(k)

print(max(dp[N-1]))


