import sys
sys.stdin = open('12852_input.txt')
input = sys.stdin.readline


def make_one(n):
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + 1
        prev[i] = i - 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3
    print(dp[n])
    print(prev)

    path= []
    while n != 0:
        path.append(n)
        n = prev[n]

    print(' '.join(map(str, path)))

n = int(input())
make_one(n)