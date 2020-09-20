# Uses merge sort to count pairs in O(nlogn)


length = int(input())
array = input().split()
array = list(map(int, array))

def pair_merge_sort(arr: list, n: int, count: int=None):
    if n <= 1:
        return arr, count

    a_length = n // 2
    b_length = n - n //2

    if count is None:
        count = 0

    a, count = pair_merge_sort(arr[:n // 2], a_length, count)
    b, count = pair_merge_sort(arr[n // 2:], b_length, count)
    c = []

    while a or b:
        if not b:
            c.append(a.pop(0))
        elif not a:
            c.append(b.pop(0))
        else:
            if a[0] < b[0]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
                count += len(a)

    return c, count

sort, pairs = pair_merge_sort(array, length)
print(pairs)
