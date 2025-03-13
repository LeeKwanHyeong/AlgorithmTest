import sys
sys.stdin = open('11399_input.txt')
input = sys.stdin.readline

N = int(input())
queue = list(map(int, input().split()))

queue.sort()
sum = 0
res = 0
for i in range(len(queue)):
    sum += queue[i]
    res += sum
print(res)