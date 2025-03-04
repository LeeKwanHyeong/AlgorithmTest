
def qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        qsort(lt, pos - 1)
        qsort(pos + 1, rt)


arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
print('Before sort : ', end = '')
print(arr)
qsort(0, 9)
print('After sort: ', end = '')
print(arr)