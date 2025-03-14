import sys
sys.stdin = open('11501_input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stock = list(map(int, input().split()))
    max_price = 0
    profit = 0

    for i in range(n-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        profit += max_price - stock[i]

    print(profit)

