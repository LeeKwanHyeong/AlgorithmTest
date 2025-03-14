import sys
sys.stdin = open('2847_input.txt')
input = sys.stdin.readline

N = int(input())
score_list = []

for _ in range(N):
    score_list.append(int(input()))

res = 0
for i in range(N-1, -1, -1):
    if i != 0:
        if score_list[i] <= score_list[i-1]:
            diff = (score_list[i] - score_list[i-1] - 1)
            score_list[i-1] += diff
            res += diff

print(abs(res))

