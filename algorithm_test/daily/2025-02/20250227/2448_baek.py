import sys

sys.stdin = open('2448_input.txt')
N = int(sys.stdin.readline())

def draw_star(n, x, y, matrix):
    if n == 3:
        matrix[y][x] = '*'
        matrix[y+1][x-1] = '*'
        matrix[y+1][x+1] = '*'
        matrix[y+2][x-2] = '*'
        matrix[y+2][x-1] = '*'
        matrix[y+2][x] = '*'
        matrix[y+2][x+1] = '*'
        matrix[y+2][x+2] = '*'
        return

    half = n // 2
    draw_star(half, x, y, matrix)  # 위쪽 삼각형
    draw_star(half, x - half, y + half, matrix)  # 왼쪽 아래 삼각형
    draw_star(half, x + half, y + half, matrix)  # 오른쪽 아래 삼각형

def print_star(n):
    matrix = [[' '] * (2*n) for _ in range(n)]
    draw_star(n, n-1, 0, matrix)
    for row in matrix:
        print("".join(row).rstrip())

print_star(N)