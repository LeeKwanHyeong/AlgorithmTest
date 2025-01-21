import sys
# from collections import deque
# sys.stdin = open('softeer/input.txt', 'r')

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# # 암기
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 방향 벡터 (상, 하, 좌, 우)

# region = [[0] * N for _ in range(N)] # 결과를 저장할 배열
# visited = [[False] * N for _ in range(N)] # 방문 여부
# region_id = 0 # 구역 번호

# def bfs(x, y, region_id):
#     queue = deque([(x, y)])
#     visited[x][y] = True
#     region[x][y] = region_id

#     while queue:
#         cx, cy = queue.popleft()

#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy

#             # 범위 안에 있고, 아직 방문하지 않은 경우
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 # 조건: 같은 구역 번호를 부여해야 하는 경우
#                 if arr[nx][ny] == arr[cx][cy]:
#                     visited[nx][ny] = True
#                     region[nx][ny] = region_id
#                     queue.append((nx, ny))

# # 보드 탐색
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]: # 방문하지 않은 칸에서 BFS 시작
#             region_id += 1 # 새로운 구역 번호 할당
#             bfs(i, j, region_id)

# print(region)

from collections import deque
sys.stdin = open('softeer/20240121/input.txt', 'r')
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def solve(N, board):
    # 결과를 저장할 배열 (구역 번호)
    region = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]  # 방문 여부 체크
    region_id = 0  # 구역 번호

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y, region_id):
        """BFS를 사용해 구역을 탐색하고 구역 번호를 할당"""
        queue = deque([(x, y)])
        visited[x][y] = True
        region[x][y] = region_id

        while queue:
            cx, cy = queue.popleft()

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy

                # 범위를 벗어나지 않고, 방문하지 않았으며, 현재 값과 같은 경우
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if board[nx][ny] == board[cx][cy]:
                        visited[nx][ny] = True
                        region[nx][ny] = region_id
                        queue.append((nx, ny))

    # 모든 칸을 탐색하면서 구역 번호 할당
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 방문하지 않은 칸에 대해 BFS 시작
                region_id += 1  # 새로운 구역 번호 부여
                bfs(i, j, region_id)

    return region

# 해결
result = solve(N, board)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
