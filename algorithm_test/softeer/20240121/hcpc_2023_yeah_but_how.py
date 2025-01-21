import sys
sys.stdin = open('softeer/20240121/input.txt', 'r')
arr = list(map(str, input().strip()))

stack = []
result = []

# ()()()

for char in arr:
    if char == '(':
        # 여는 괄호는 그대로 삽입
        result.append('(')
        stack.append(len(result) - 1) # 여는 괄호의 위치 기록
        print(f'stack: {stack}')
    elif char == ')':
        # 다는 괄호는 이전 여는 괄호와 매칭
        if stack:
            # 스택에서 가장 최근의 열린 괄호를 닫음
            idx = stack.pop()
            # 여는 괄호와 닫는 괄호 사이에 최소한 하나의 '1' 삽입
            print(f'idx:{idx} len(result):{len(result)}')
            if idx + 1 >= len(result) or result[idx + 1] != '1': # 이미 '1'이 없으면 삽입
                result.append('1')
            print(f'result: {result}')
        result.append(')') # 닫는 괄호 삽입
        result.append('+')

result.pop()
a = ''.join(result)
print(a)
