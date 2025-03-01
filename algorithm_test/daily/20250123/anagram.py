import sys

sys.stdin = open('daily/20250123/input.txt')

a = input()
b = input()

# str1 = dict()
# str2 = dict()

# for x in a:
#     str1[x] = str1.get(x, 0) + 1

# for x in b:
#     str2[x] = str2.get(x, 0) + 1

# for i in str1.keys():
#     if i in str2.keys() and str1[i] == str2[i]:
#         continue
#     else:
#         print('NO')
#         break

# else: 
#     print('YES')

sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print('NO')
        break
else:
    print('YES')

