import sys
from collections import deque

sys.stdin = open('daily/20250225/1021_input.txt')

N, M = map(int, sys.stdin.readline().strip().split())
targets = list(map(int, sys.stdin.readline().split()))

queue = deque(range(1, N+1))

move_count = 0

for target in targets:
    idx = queue.index(target)

    if idx < len(queue) - idx:
        queue.rotate(-idx)
        move_count += idx

    else:
        queue.rotate(len(queue) - idx)
        move_count += len(queue) - idx

    queue.popleft()

print(move_count)