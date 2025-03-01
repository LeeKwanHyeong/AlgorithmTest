import sys

# <정렬방식>
# 1. 국어 점수가 감소순
# 2. 국어 점수가 같으면 영어 점수가 증가순
# 3. 국어 점수 영여 점수 같으면 수학 점수 감소순
# 4. 모든 점수가 같으면 이름이 사전 순

sys.stdin = open('daily/20250221/10825_input.txt')

N = int(sys.stdin.readline())
# p = dict({input(): 1 for _ in range(N)})
dict = {}

for _ in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    dict[name] = [int(kor), int(eng), int(math)]

print(dict)
# 정렬 기준 (-국어, +영어, -수학, +이름)
result = sorted(dict.items(), key = lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

for name, scores in result:
    print(name)
