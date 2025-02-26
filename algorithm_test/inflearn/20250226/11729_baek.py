import sys

sys.stdin = open('inflearn/20250226/11729_input.txt')

N = int(sys.stdin.readline())

# 힌 반에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
def hanoi(n, from_pole, to_pole, aux_pole, moves):
    if n == 1:
        moves.append((from_pole, to_pole))
        return
    hanoi(n-1, from_pole, aux_pole, to_pole, moves)
    moves.append((from_pole, to_pole))
    hanoi(n - 1, aux_pole, to_pole, from_pole, moves)

moves = []
hanoi(N, 1, 3, 2, moves)

print(len(moves))
for move in moves:
    print(*move)