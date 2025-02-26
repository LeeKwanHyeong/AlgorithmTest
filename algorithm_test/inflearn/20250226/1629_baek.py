import sys

sys.stdin = open('inflearn/20250226/1629_input.txt')

A, B, C = map(int, sys.stdin.readline().split())

print(pow(A, B, C))