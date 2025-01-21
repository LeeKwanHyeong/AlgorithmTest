import sys

sys.stdin = open('softeer/20240121/input.txt', 'r')
n , m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
f_attack_start, f_attack_end = map(int, input().split())
s_attack_start, s_attack_end = map(int, input().split())
res = 0

for i in range(f_attack_start - 1, f_attack_end):
    for k in range(m):
        if arr[i][k] == 1:
            arr[i][k] = 0
            break

for i in range(s_attack_start - 1, s_attack_end):
    for k in range(m):
        if arr[i][k] == 1:
            arr[i][k] = 0
            break

for i in arr:
    res += i.count(1)

print(res)
