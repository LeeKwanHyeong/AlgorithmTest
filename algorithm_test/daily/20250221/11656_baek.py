import sys

sys.stdin = open('daily/20250221/11656_input.txt')

d = sys.stdin.readline().strip()
dict_list = [d[i::] for i in range(0, len(d))]
dict_list.sort()
for i in dict_list:
    print(i)