"""
PA3 Problem 2
Justin Huang (jfh5730)
Divyesh Johri (dkj5225)
Eddie Ubri (evu5018)
"""

import heapq
from collections import defaultdict

n, m, s = list(map(int, input().split())) # n vertices, m edges, s = source vertex

g = defaultdict(list)

for _ in range(m):
    a, b, c = list(map(int, input().split())) # edge (a, b) with length c
    g[a].append((b, c)) # stored as (vertex, length)

def dijkstra(g, s):
    dist = [float('inf') for _ in range(n)]
    dist[s - 1] = 0
    pq = [(0, s)] # importantly stored as (length, vertex) to maintain priority queue as opposed to g (vertex, length)
    for v in g:
        if v == s:
            continue
        pq.append((float('inf'), v))
    while len(pq):
        current_dist, u = heapq.heappop(pq)
        for v, l in g[u]:
            if dist[v - 1] > dist[u - 1] + l:
                dist[v - 1] = dist[u - 1] + l
                decrease_key(pq, v, dist[v - 1])
    return dist

def decrease_key(pq, v, value):
    for i in range(len(pq)):
        l, u = pq[i]
        if u == v:
            pq[i] = (value, v)
            heapq.heapify(pq)
            return

dist = dijkstra(g, s)
for d in dist:
    if d == float('inf'):
        d = -1
    print(d)
