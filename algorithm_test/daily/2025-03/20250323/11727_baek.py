import sys
sys.stdin = open('11727_input.txt')
input = sys.stdin.readline

N = int(input())

a = 1
b = 3

for i in range(3, N+1):
    a, b = b, a*2 + b


print(b % 10007)