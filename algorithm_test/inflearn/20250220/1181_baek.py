import sys

# 알파벳 소문자로 이루어진 N개 단어
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전순으로

sys.stdin = open('inflearn/20250220/1181_input.txt')

N = int(sys.stdin.readline())

str_list = list(set(sys.stdin.readline().strip() for _ in range(N)))
print(str_list)

str_list.sort(key = lambda x: (len(x), x))

for i in str_list:
    print(i)