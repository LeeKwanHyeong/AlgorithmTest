import sys
from collections import deque
sys.stdin = open('1026_input.txt')
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()
sum = 0
for i in range(N):
    sum += A[i] * B[i]

print(sum)