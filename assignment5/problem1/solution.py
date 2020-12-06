n = int(input())

intervals = []  # populate with [start, finish, value]
for i in range(n):
    intervals.append(list(map(int, input().split())))

def binary_search(A, k, a, b):
    m = (a + b) // 2
    # print(m, A[m][1], A[k][0], A[m+1][1])
    if a == b:
        if A[m][1] <= A[k][0] < A[m + 1][1]:  # pre[k] = m
            return m
        return -1

    if A[m][1] <= A[k][0] < A[m + 1][1]:  # pre[k] = m
        return m
    elif A[m][1] > A[k][0]:
        return binary_search(A, k, a, m)
    elif A[k][0] >= A[m + 1][1]:
        return binary_search(A, k, m + 1, b)
    else:
        return -1

def DP_weighted(A, n):
    sorted_A = finish_merge_sort(A, n)
    F = [0, sorted_A[0][2]]
    for i in range(1, n):
        pre = binary_search(sorted_A, i, 0, i - 1)
        F.append(max(F[i], F[pre + 1] + sorted_A[i][2]))
        # print(i, F[-1])
    # print(F)
    return F[n]

def finish_merge_sort(A, n):
    if n <= 1:
        return A

    n_a = n // 2
    n_b = n - n // 2

    a = finish_merge_sort(A[:n_a], n_a)
    b = finish_merge_sort(A[n_a:], n_b)
    c = []

    while a or b:
        if not b:
            c.append(a.pop(0))
        elif not a:
            c.append(b.pop(0))
        else:
            # favor earlier start time in case of tie
            if a[0][1] < b[0][1] or (a[0][1] == b[0][1] and a[0][0] < b[0][0]):
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))

    return c

if n == 0:
    print(0)
elif n == 1:
    print(intervals[0][2])
else:
    # print(finish_merge_sort(intervals, n))
    print(DP_weighted(intervals, n))
