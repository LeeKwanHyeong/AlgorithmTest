import sys
sys.stdin = open('daily/20250224/10828_input.txt')

N = int(sys.stdin.readline())
temp = []

for i in range(N):
    line = sys.stdin.readline().strip().split()

    name, *value = line
    value = value[0] if value else None

    if name == 'push':
        temp.append(value)
    elif name == 'pop':
        if temp:
            a = temp.pop()
            print(a)
        else:
            print(-1)
    elif name == 'size':
        print(len(temp))
    elif name == 'empty':
        if temp:
            print(0)
        else:
            print(1)
    elif name == 'top':
        if temp:
            print(temp[-1])
        else:
            print(-1)
    else:
        print(0)
