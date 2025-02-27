import sys

sys.stdin = open('1992_input.txt')

N = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]

def compress_quad_tree(x, y, size, matrix):
    # 현재 영역이 모두 같은 숫자인지 확인
    first = matrix[x][y]
    same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != first:
                same = False
                break
        if not same:
            break

    # 모두 같은 숫자라면 해당 숫자 반환
    if same:
        return first

    # 4개 영역으로 나뉘어 재귀적으로 압축 수행
    half = size // 2
    upper_left = compress_quad_tree(x, y, half, matrix) # 왼쪽 위
    upper_right = compress_quad_tree(x, y + half, half, matrix) # 오른쪽 위
    lower_left = compress_quad_tree(x + half, y, half, matrix) # 왼쪽 아래
    lower_right = compress_quad_tree(x + half, y + half, half, matrix) # 오른쪽 아래

    return f'({upper_left}{upper_right}{lower_left}{lower_right})'

result = compress_quad_tree(0, 0, N, matrix)

print(result)