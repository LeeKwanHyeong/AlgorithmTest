import sys

sys.stdin = open('daily/20250123/input.txt')

N = int(input())

p = dict({input(): 1 for _ in range(N)})
p.update({input():0 for _ in range(N-1)})
print(p)

for key, val in p.items():
    if val == 1:
        print(key)
        break