import sys
sys.stdin =  open('inflearn/20250122/input.txt', 'r')
a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if x == '+':
            stack.append(n2 + n1)
        elif x == '-':
            stack.append(n2 - n1)
        elif x == '*':
            stack.append(n2 * n1)
        elif x == '/':
            stack.append(n2 / n1)
print(stack[0])