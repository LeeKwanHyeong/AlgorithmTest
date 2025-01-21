import sys

# 진정한 효도
# 풀이 전략: 가로로 3 혹은 세로로 3을 통해 토지의 높낮이를 낮추고 올려 그 중에 최솟값을 구한다.

# Input     Input
# 1 1 1     1 1 3
# 2 3 1     1 1 3
# 3 1 2     3 3 1
# Output    Output
# 0         2

# 놓친 부분: 문제를 제대로 안읽음. "남우가 특정 땅 높이를 1만큼 '낮추거나' '높이는데' 1만큼의 비용이 소모된다고...."

sys.stdin = open('softeer/20240121/input.txt', 'r')

land = [list(map(int, input().split())) for _ in range(3)]
cost = 100

def min_filter(cost, i, j, k):
    value = 0
    # i에 맞춰서 올리고 내리는거
    i_value = abs(i - j)
    i_value += abs(i - k)
    # j에 맞춰서 올리고 내리는거
    j_value = abs(j - i)
    j_value += abs(j - k) 
    # k에 맞춰서 올리고 내리는거
    k_value = abs(k - i)
    k_value += abs(k - j)
    value = min(i_value, j_value, k_value)
    cost = min(value, cost)
    return cost


for row in land:
    i, j, k = row[0], row[1], row[2]
    cost = min_filter(cost, i, j, k)

for index in range(3):
    i, j, k = land[0][index], land[1][index], land[2][index]
    cost = min_filter(cost, i, j, k)
    
print(cost)