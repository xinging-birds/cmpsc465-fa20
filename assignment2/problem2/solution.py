def graham_scan(p: list):
    # find point with smallest y-coordinate
    min_i = 0
    dupl = -1
    for i in range(1, len(p)):
        if p[i][1] < p[min_i][1]:
            min_i = i
        elif p[i][1] == p[min_i][1]:
            dupl = i
    if dupl != -1:
        min_i = dupl if p[dupl][0] < p[min_i][0] else min_i
    
    p0 = p.pop(min_i)
    n = len(p)
    # sort in ascending order of angles wrt p0 and (infty, 0) by using cosine
    p = angle_merge_sort(p, n, p0)
    p.insert(0, p0)
    p_prime = graham_scan_core(p, n + 1)
    return p_prime


def graham_scan_core(p: list, n: int):
    if n <= 3:
        return p
    
    stack = []
    stack.append(p[0])
    stack.append(p[1])
    stack.append(p[2])
    for i in range(3, n):
        while len(stack):
            pa, pb = stack[-1], stack[-2]
            a, b = [pa[0]-pb[0], pa[1]-pb[1]], [p[i][0]-pa[0], p[i][1]-pa[1]]
            orientation = a[0] * b[1] - b[0] * a[1]  # cross product as determinant
            if orientation < 0:
                stack.pop()
            else:
                break
        stack.append(p[i])
    return stack


def angle_merge_sort(p: list, n: int, p0: list):
    if n <= 1:
        # add angle to the element p
        vector = [p[0][0]-p0[0], p[0][1]-p0[1]]
        p[0].append(vector[0] / ((vector[0] ** 2 + vector[1] ** 2) ** (1/2)))
        return p

    a_length = n // 2
    b_length = n - n //2

    a = angle_merge_sort(p[:n // 2], a_length, p0)
    b = angle_merge_sort(p[n // 2:], b_length, p0)
    c = []

    while a or b:
        if not b:
            c.append(a.pop(0))
        elif not a:
            c.append(b.pop(0))
        else:
            if a[0][2] > b[0][2]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
    
    return c


n = int(input())  # number of lines
duals = []
for i in range(n):
    dual = list(map(float, input().split()))
    dual[1] *= -1
    duals.append(dual)

hull = graham_scan(duals)
upper, lower = 0, 0
left, right = min(hull, key=lambda x:x[0]), max(hull, key=lambda x:x[0])
left_i, right_i = hull.index(left), hull.index(right)

for j in range(len(hull)):
    if j == left_i or j == right_i:
        upper += 1
        lower += 1
    elif right_i > left_i:
        if left_i < j < right_i:
            upper += 1
        else:
            lower += 1
    else:
        if right_i < j < left_i:
            lower += 1
        else:
            upper += 1
print(upper, lower)
