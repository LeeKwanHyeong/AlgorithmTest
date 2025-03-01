import sys
sys.stdin = open('input.txt', 'rt')
# card_list = [ i for i in range(1, 21) ]
card_list = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        card_list[s + i], card_list[e - i] = card_list[e - i], card_list[s + i]

card_list.pop(0)
print(card_list)