import sys
from collections import Counter

# 현우가 강산이에게 보내는 메시지
# 메시지는 숫자 N개로 이루어진 수열
# 숫자는 모두 C보다 작거나 같다. 창영이는 이 숫자를 자주 등장하는 빈도순서대로 정렬하고자함
# 만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는경우에는 X가 Y보다 앞에
# 횟수가 같다면 먼저 나온 것이 앞에 있어야 한다.
sys.stdin = open('daily/20250220/2910_input.txt')

N, C = map(int, sys.stdin.readline().split())

iter = list(map(int, sys.stdin.readline().split()))
counter = Counter(iter)
print(counter)
sorted_counter = counter.most_common()


result = [str(key) for key, value in sorted_counter for _ in range(value)]
print(" ".join(result))

