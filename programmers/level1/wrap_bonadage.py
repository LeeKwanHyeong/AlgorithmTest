# [PCCP 기출 문제] 1번 / 붕대감기
# 시간의 흐름에 따라 이벤트를 처리하는 "시뮬레이션 유형"
# 각 라운드(시간)마다 회복과 공격 이벤트가 발생, 이를 정확히 처리하는 것이 핵심
# "그리디 알고리즘"으로써, 매 라운드마다 최적의 행동(공격 처리, 체력 회복)을 선택해야 한다.
# "이진 탐색" 활용 가능, 만약 공격 이벤트가 매우 많아지고 특정 라운드의 이벤트를 빠르게 찾아야 한다면, 이진 탐색을 사용할 수 있다.
# 해당 문제는 "이벤트 기반 처리"로써, 
# 1. 현재 시간이 공격 이벤트의 시간과 일치하면, 해당 공격을 처리
# 2. 공격 이벤트가 없으면 회복 이벤트 처리
# 3. 체력이 0 이하면 즉시 종료
# 4. 시간이 흐를수록 업데이트

bondage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]

def solution(bandage, health, attacks):
    t, x, y = bandage #시전시간, 초당 회복량, 추가 회복량
    hp = health # 체력값 초기: 풀체
    continuous = 0 # 기술 시전 횟수
    attack_index = 0 # 현재 공격 처리 인덱스

    for i in range(1, attacks[-1][0] + 2): # 마지막 공격 시간까지 반복
        print(f'Round{i}')
        if i == attacks[-1][0] + 1:
            break

        # 공격
        if attack_index < len(attacks) and attacks[attack_index][0] == i:
            damage = attacks[attack_index][1]
            hp -= damage
            attack_index += 1
            continuous = 0
            print(f'Attacked:{damage} HP:{hp}')

            # 체력이 0 이하면 종료
            if hp <= 0:
                print('Attacked: Dead')
                return -1
            continue
            
            # 공격 받은 경우 회복하지 않음

        if continuous < t:
            hp = min(health, hp + x) # 초당 회복량
            continuous += 1
            print(f'Bondage Finish: {hp}, Continuous: {continuous}')
        if continuous == t:
            hp = min(health, hp + y) # 추가 회복량
            continuous = 0
            print(f'Bondage Skill: {hp}')

    print(hp)
    return hp

solution(bondage, health, attacks)