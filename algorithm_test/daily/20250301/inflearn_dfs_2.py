import sys
sys.stdin = open('inflearn_dfs_2_input.txt')

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end = ' ')
        DFS(v * 2)
        DFS(v * 2 + 1)


DFS(1)