import sys
sys.stdin = open('1541_input.txt')
input = sys.stdin.readline

expression = input().strip()

split_minus = expression.split('-')

print(split_minus)

result = sum(map(int, split_minus[0].split('+')))

for part in split_minus[1:]:
    result -= sum(map(int, part.split('+')))

print(result)