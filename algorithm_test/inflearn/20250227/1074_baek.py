import sys
sys.stdin = open("1074_input.txt")

# 2^N x 2^N 배열을 Z 모양 탐색

def z_search(N, r, c):
    if N == 0:
        return 0

    half = 2 ** (N-1)
    quadrant_size = half * half

    # 왼쪽 위 (0번째 영역)
    if r < half and c < half:
        return z_search(N - 1, r, c)

    # 오른쪽 위 (1번째 영역)
    elif r < half and c >= half:
        return quadrant_size + z_search(N-1, r, c - half)

    # 왼쪽 아래 (2번째 영역)
    elif r >= half and c < half:
        return 2 * quadrant_size + z_search(N - 1, r - half, c)

    # 오른쪽 아래 (3번째 영역)
    else:
        return 3 * quadrant_size + z_search(N-1, r - half, c - half)

N, r, c = map(int, input().split())

print(z_search(N, r, c))
