import sys
sys.stdin = open('1912_input.txt')
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

current_sum = max_sum = seq[0]

for i in range(1, n):
    current_sum = max(seq[i], current_sum + seq[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
