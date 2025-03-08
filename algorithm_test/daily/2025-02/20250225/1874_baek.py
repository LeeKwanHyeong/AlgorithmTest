import sys

sys.stdin = open('daily/20250225/1874_input.txt')
n = int(sys.stdin.readline().strip())
target = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
result = []
current = 1  # 스택에 push할 숫자 (1부터 시작)

for num in target:
    while current <= num:  # 목표 숫자까지 push
        stack.append(current)
        result.append('+')
        current += 1
    
    if stack[-1] == num:  # 스택에서 pop할 숫자가 일치하면 pop 수행
        stack.pop()
        result.append('-')
    else:  # 스택의 top과 num이 다르면 만들 수 없는 수열 (불가능한 경우)
        print("NO")
        exit()

# 결과 출력
print("\n".join(result))