import sys

sys.stdin = open('inflearn/20250122/input.txt', 'r')

batch = list(map(str, input().strip()))
sum = 0
stack = []

for s in batch:
    if s == ')' and stack:
        if stack:
            stack.pop()
            sum += len(stack)
    else: 
        stack.append(s)
    print(f'sum = {sum} stack: {stack}')

print(sum)