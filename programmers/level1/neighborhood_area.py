# 주요 쟁점 : 2D 배열 + 경계조건 설정
# 주요 알고리즘: Flood Fill 알고리즘
# 정의: Flood Fill은 특정 위치에서 시작해, 상하좌우(또는 대각선 포함)로 연결된 영역을 탐색하며, 조건에 따라 연결된 영역을 처리하는 알고리즘
# 문제 확장 한다면 대각선 탐색까지
# if x >= 1 and y >= 1:  # 좌상단 대각선
#     if color == board[x - 1][y - 1]:
#         count += 1
# if x >= 1 and y + 1 < max_y:  # 우상단 대각선
#     if color == board[x - 1][y + 1]:
#         count += 1
# if x + 1 < max_x and y >= 1:  # 좌하단 대각선
#     if color == board[x + 1][y - 1]:
#         count += 1
# if x + 1 < max_x and y + 1 < max_y:  # 우하단 대각선
#     if color == board[x + 1][y + 1]:
#         count += 1


board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1
result = 2

def solution(board, x, y):
    
    count = 0
    max_x, max_y = len(board), len(board[0])
    color = board[x][y]
    
    # 위 : [x-1][y] 아래: [x+1][y] 좌: [x][y-1] 우: [y][y+1]
    
    # 위
    if x >= 1:
        if color == board[x - 1][y]:
            count += 1
    # 아래
    if x + 1 <= max_x - 1:
        if color == board[x+1][y]:
            count += 1
    # 좌
    if y >= 1:
        if color == board[x][y - 1]:
            count += 1
    # 우
    if y + 1 <= max_y - 1:
        if color == board[x][y + 1]:
            count += 1
    
    
    return count

result = solution(board, h, w)
print(result)