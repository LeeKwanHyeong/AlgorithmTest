import sys
sys.stdin = open('inflearn/20250220/10814_input.txt')

N = int(sys.stdin.readline())
list = [tuple(map(str, sys.stdin.readline().split())) for _ in range(N) ]

list.sort(key=lambda x: int(x[0]), reverse=False)
for i in list:
    print(f'{i[0]} {i[1]}')

