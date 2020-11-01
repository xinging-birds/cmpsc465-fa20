"""
PA4 Prob 1
Justin Huang (jfh5730)
Divyesh Johri (dkj5225)
Eddie Ubri (evu5018)
"""

from collections import defaultdict

n, m, s = list(map(int, input().split())) # n vertices, m edges, s = source vertex

g = defaultdict(list)

for _ in range(m):
    a, b, c = list(map(int, input().split())) # edge (a, b) with length c
    g[a].append((b, c)) # stored as (vertex, length)
