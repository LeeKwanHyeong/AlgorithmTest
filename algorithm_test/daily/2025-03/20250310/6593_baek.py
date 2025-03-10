import sys
from collections import deque

sys.stdin = open('6593_input.txt')
input = sys.stdin.readline

dh, dx, dy = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)

# 지나갈 수 없는 칸: # 비어있는 칸 : . 시작 지점: S 출구: E


# 입력 데이터 전체 읽기
data = sys.stdin.read().strip()

# 입력 데이터가 없을 경우 종료
if not data:
    sys.exit(0)

# 개행 문자 단위로 줄 분리
lines = data.split("\n")
index = 0


def bfs(start_h, start_x, start_y):
    queue = deque([(start_h, start_x, start_y, 0)])
    visited[start_h][start_x][start_y] = True

    while queue:
        h, x, y, time = queue.popleft()

        if building[h][x][y] == 'E':
            return f'Escaped in {time} minute(s).'

        for i in range(6):
            nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]

            if 0 <= nh < L and 0 <= nx < R and 0 <= ny < C:
                if not visited[nh][nx][ny] and building[nh][nx][ny] != '#':
                    visited[nh][nx][ny] = True
                    queue.append((nh, nx, ny, time + 1))
    return 'Trapped!'


while index < len(lines):
    # 층 수, 행 수, 열 수 읽기
    try:
        L, R, C = map(int, lines[index].split())
    except ValueError:
        break  # 잘못된 입력이 있으면 종료

    # 종료 조건 (0 0 0)
    if L == 0 and R == 0 and C == 0:
        break

    index += 1  # 다음 줄 이동
    building = []
    start_position = None
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]

    # 3D 리스트 생성 (L층 * R행 * C열)
    for floor_idx in range(L):
        floor = []
        for row_idx in range(R):
            floor.append(list(lines[index]))
            for col_idx in range(C):
                if floor[row_idx][col_idx] == 'S':
                    start_position = (floor_idx, row_idx, col_idx)
            index += 1
        building.append(floor)
        index += 1

    # BFS 실행 및 결과 출력
    if start_position:
        print(bfs(*start_position))
