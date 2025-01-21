# 바이러스
# 바이러스는 숙주의 몸속에서 1초당 P배씩 증가
# 2 3 2

import sys
sys.stdin = open('softeer/20240121/input.txt', 'r')


# MOD = 1000000007
# K, P, N = map(int, input().split())
# result = (K * P ** N) % MOD

# print(result)

# 위 코드는 효율성의 문제가 생길 수 있다.
# P ** N  의 계산은 거듭제곱 연산으로, N이 매우 클 경우 P**N이 매우 큰 값이 되어 메모리 초과나 연산 속도 문제를 야기할 수 있다.
# 파이썬의 int는 무제한 정수를 지원하므로 값이 커져도 메모리 문제가 발생하지 않을 수 있지만, 계산 비용이 커질 수 있다.

# 아래 코드는 P ** N을 직접 계산하지 않고, 반복문을 통해 P**N mode MOD를 점진적으로 계싼한다.
# 각 단계에서 모듈러 연산을 수행하기 때문에 P**N의 값이 매우 커지는 것을 방지 할 수 있다.
# 연산 과정에서 결과가 MOD보다 커지는 것을 방지하므로 메모리와 계산 비용을 줄인다.
# 시간 복잡도는 O(N)이며, 메모리 사용량도 제한적이다.


def calculate_virus_count(K, P, N):
    MOD = 1000000007
    result = K
    for i in range(1, N+1):
        result = (result * P) % MOD
    return result


K, P, N = map(int, input().split())
result = calculate_virus_count(K, P, N)
print(result)

