import sys
from collections import deque

sys.stdin = open('daily/20250225/10866_input.txt')

N = int(sys.stdin.readline())
result = deque()

for i in range(N):
    line = sys.stdin.readline().strip().split()

    name, *value = line
    value = value[0] if value else None

    if name == 'push_front':
        result.appendleft(value)
    elif name == 'push_back':
        result.append(value)
    elif name == 'pop_front':
        if result:
            print(result.popleft())
        else:
            print(-1)
    elif name == 'pop_back':
        if result:
            print(result.pop())
        else:
            print(-1)
    elif name == 'size':
        print(len(result))
    elif name == 'empty':
        if result:
            print(0)
        else:
            print(1)
    elif name == 'front':
        if result:
            print(result[0])
        else:
            print(-1)
    elif name == 'back':
        if result:
            print(result[-1])
        else:
            print(-1)