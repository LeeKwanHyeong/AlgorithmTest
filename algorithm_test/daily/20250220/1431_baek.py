import sys

# 시리얼 번호 실버3
# 각각 기타는 모두 다른 시리얼 번호를 가지고 있다. 기타를 빨리 찾아서 
# 빨리 사람들에게 연주해주기 위해 시리얼 번호 순서대로 정렬하고자 한다.
# 모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.

# 1. A와 B의 길이가 다르면, 짧은 것 먼저
# 2. 길이가 같다면 A의 모든 자리수의 합과 B의 모든 자리수 합 비교
# 3. 만약 1, 2 번 조건으로 비교 불가능 하면 사전순으로 비교

def sum_of_digits(s):
    return sum(int(c) for c in s if c.isdigit())

sys.stdin = open("daily/20250220/1431_input.txt")
N = int(input())

serial = [input() for _ in range(N)]
serial.sort(key = lambda x: (len(x), sum_of_digits(x), x))
for i in serial:
    print(i)