# 연습문제
# 기존 코드
# def solution(n, m, section):
#     answer = 0
#     total_len = [1] * n

#     # section의 값으로 total_len 초기화
#     for sector in section:
#         total_len[sector - 1] = 0

#     # 0이 있는 동안 반복
#     while 0 in total_len:
#         # 가장 앞의 0 위치 찾기
#         index = total_len.index(0)
#         answer += 1  # 롤러 사용 횟수 증가

#         # 롤러로 덮는 범위 처리
#         for i in range(m):
#             if index + i < n:  # 범위 초과 방지
#                 total_len[index + i] = 1

#     return answer

# 효율성을 높이기 위한 개선 방법
# 1. 리스트 탐색 최소화:
#  - total_len 리스트 대신, section 리스트 자체를 사용하여 0의 위치를 관리
#  - 롤러가 덮을 범위를 계산하고, 덮인 구역은 section 리스트에서 제거
# 2. 정렬 및 범위 관리
#  - section은 이미 입력값으로 정렬된 상태라면, 앞에서부터 순차적으로 처리하여 시간을 절약할 수 있다.

def solution(n, m, section):
    answer = 0
    i = 0  # 현재 처리 중인 section의 인덱스

    while i < len(section):
        # 현재 롤러로 덮을 수 있는 최대 범위 계산
        start = section[i]
        end = start + m - 1
        answer += 1  # 롤러 사용 횟수 증가

        # 현재 롤러 범위에 포함된 구역 건너뛰기
        while i < len(section) and section[i] <= end:
            i += 1

    return answer