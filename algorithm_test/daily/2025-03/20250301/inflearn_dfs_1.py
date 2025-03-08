import sys

sys.stdin = open('inflearn_dfs_1_input.txt')

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end = ' ')

N = int(sys.stdin.readline())
DFS(N)
