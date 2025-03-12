import sys
sys.stdin = open('9466_input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    global count
    stack = [node]
    cycle = []

    while stack:
        node = stack.pop()
        if visited[node]:
            if node in cycle:
                count -= len(cycle[cycle.index(node):])
            return
        visited[node] = True
        cycle.append(node)
        stack.append(graph[node])

T = int(input())

for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    count = n

    for i in range(1, n +1):
        if not visited[i]:
            dfs(i)
    print(count)