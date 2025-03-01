import sys
from collections import Counter
# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램

sys.stdin = open('daily/20250220/11652_input.txt')

N = int(sys.stdin.readline().strip())
cards = [int(sys.stdin.readline().strip()) for _ in range(N)]

counter = Counter(cards)
print(counter)
# - max를 사용할 때 key 기준을 (빈도수, 숫자의 음수 값)으로 설정
# - 동일한 빈도가 있다면 음수 값이 더 큰 (=원래 값이 작은) 숫자가 우선됨
#  1) counter[x] -> 등장 빈도 기준 정렬
#  2) -x -> 빈도가 같다면 숫자가 작은 것을 선택

most_common_num = max(counter.keys(), key=lambda x: (counter[x], -x))

print(most_common_num)
