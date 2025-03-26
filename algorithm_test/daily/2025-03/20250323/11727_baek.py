import sys
sys.stdin = open('11727_input.txt')
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    sys.exit(0)

a = 1
b = 3

for i in range(3, N+1):
    a, b = b, a*2 + b


print(b % 10007)