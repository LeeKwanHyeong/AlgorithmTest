import sys

sys.stdin = open('softeer/20240121/input.txt', 'r')
n = int(input())
arr = [input() for _ in range(n)]

def custom_sort_key(number):
    if '.' in number:
        int_part, decimal_part = number.split('.')
        return (int(int_part), int(decimal_part))
    else:
        return(int(number), -1)
    

sorted_numbers = sorted(arr, key=custom_sort_key)

print('\n'.join(sorted_numbers))
                



