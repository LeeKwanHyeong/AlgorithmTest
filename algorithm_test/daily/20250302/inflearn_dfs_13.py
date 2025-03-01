import sys
import itertools as it
sys.stdin = open('inflearn_dfs_13_input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1


print(cnt)
