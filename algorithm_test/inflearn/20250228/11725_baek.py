import sys
from collections import defaultdict

sys.stdin = open('11725_input.txt')

sys.setrecursionlimit(10 ** 6)
N = int(sys.stdin.readline().strip())
graph = defaultdict(list) # 트리 그래프 저장
parent = [0] * (N + 1) # 부모 정보를 저장할 리스트 (0으로 초기화)


def find_parents(node):
    for child in graph[node]:
        if parent[child] == 0: # 아직 방문하지 않은 노드라면
            parent[child] = node # 부모 저장
            find_parents(child) # 재귀 호출 (DFS)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 그래프 저장 (무방향 트리)

# DFS 탐색 수행 (루트는 1번)
parent[1] = -1 # 루트 노드(1)의 부모는 없음
find_parents(1)

print(graph)
# 결과 출력 (2번 노드부터 N번 노드까지 부모 출력)
for i in range(2, N + 1):
    print(parent)
    print(parent[i])