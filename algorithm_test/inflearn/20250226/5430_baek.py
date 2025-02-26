import sys
import json
from collections import deque
sys.stdin = open('inflearn/20250226/5430_input.txt')

# R(뒤집기) D(버리기)
# R: 배열에 있는 수의 순서를 뒤집는 함수
# D: 첫 번째 수를 버리는 함수
# 배열이 비어있는데 D를 사용한 경우에는 에러
# "AB"는 A를 수행한 후, 바로 이어서 B를 수행

T = int(sys.stdin.readline())


for case in range(T):
    sequence = sys.stdin.readline()
    size = int(sys.stdin.readline())
    lst = deque(json.loads(sys.stdin.readline()))
    is_reversed = False
    for s in sequence:
        if s == 'R':
            is_reversed = not is_reversed
        elif s == 'D':
            if lst:
                if is_reversed:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                print('error')
                break
    else:
        if is_reversed:
            lst.reverse()
        
        print("[" + ",".join(map(str, lst)) + "]")
    
    