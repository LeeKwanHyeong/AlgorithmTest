import sys

sys.stdin = open('inflearn/20250220/5648_input.txt')

# 모든 원소가 양의 정수인 집합
# 원소를 거꾸로 뒤집고 그 원소를 오름차순으로 정렬하는 프로그램
# 단 원소를 뒤집었을 때 0이 앞에 선행되는 경우는 0을 생략
N_list = sys.stdin.readline().split()
N = N_list.pop(0)
data = sys.stdin.read().splitlines()
temp = []

for i in N_list:
    temp.append(int(i[::-1]))

for line in data:
    a = line.split()
    for i in a:
        temp.append(int(i[::-1]))
temp.sort()

for i in temp:
    print(i)
