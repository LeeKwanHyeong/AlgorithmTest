import sys
import math

sys.stdin = open('2447_input.txt')

N = int(sys.stdin.readline())
matrix = [['*' for _ in range(N)] for _ in range(N)]


def star_remove(N, x, y, matrix):
    if N == 1:
        return

    size = N // 3 # 3등분 크기
    for i in range(size, 2 * size):
        for j in range(size, 2 * size):
            matrix[x + i][y + j] = " "

    for dx in range(3):
        for dy in range(3):
            if dx == 1 and dy == 1:
                continue
            star_remove(size, x + dx * size, y + dy * size, matrix)

def print_star(N):
    matrix = [['*'] * N for _ in range(N)]
    star_remove(N, 0, 0, matrix)
    for row in matrix:
        print("".join(row))

print_star(N)






