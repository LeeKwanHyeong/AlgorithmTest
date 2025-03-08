import sys
import bisect
sys.stdin = open('daily/20250224/7795_input.txt')

# A는 자기보다 크기가 작은 먹이만 먹을 수 있다.

T = int(sys.stdin.readline())
for case in range(T):
    count = 0
    N, M = map(int, sys.stdin.readline().split())
    a_size = list(map(int, sys.stdin.readline().split()))
    b_size = list(map(int, sys.stdin.readline().split()))
    a_size.sort()
    b_size.sort()

    for a in a_size:
        idx = bisect.bisect_right(b_size, a - 1)
        count += idx
    
    print(count)
