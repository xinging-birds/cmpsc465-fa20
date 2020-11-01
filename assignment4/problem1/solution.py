"""
PA4 Prob 1
Justin Huang (jfh5730)
Divyesh Johri (dkj5225)
Eddie Ubri (evu5018)
"""

from collections import defaultdict
import array as arr 

# Modified DP algorithm with one extra row
# Inputs: Graph g = (V, E), n = |V|, s = source vertex
# Outputs: DP table of subproblems dist
# Runtime: O(|V|*|E|)
def dp_shortest_path(g, n, s):

    # Subproblem dist n x n DP table
    # Set dist[0,s] to 0 and initialize the rest to infinity
    dist = [ [float('inf') for _ in range(n)] for _ in range(n) ]
    dist[0][0] = 0

    arrMap = {}
    i = 0
    for v in g:
        arrMap[v] = i
        i = i + 1

    print(arrMap)
    
    # Recursively solve the subproblem dist[k][v]
    for k in range(1, len(g)):   # not n-1, as we need one extra row
        for v in range(len(g)):
            dist[k][v] = dist[k-1][v]
            for u, l in g[v]:
                if(dist[k][v] > dist[k-1][arrMap[u]] + l):
                    dist[k][v] = dist[k-1][arrMap[u]] + l
    
    # Return DP table
    return dist

# Algorithm to find negative cycles
# Inputs: Graph g = (V, E), n = |V|, s = source vertex
# Outputs: True -> g has negative cycle
#          False -> g doesn't have a negative cycle
# Runtime: O(|V|*|E|) due to DP algorithm
def detect_negative_cycle(g, n, s):
    dist = dp_shortest_path(g, n, s)
    if(dist[len(g),v] for v in range(len(g)) == dist[n-1,v] for v in range(len(g))):
        return False
    else:
        return True


# Obtain graph information
n, m, s = list(map(int, input().split())) # n vertices, m edges, s = source vertex

# Make the graph
g = defaultdict(list)
given_vs = []
possible_vs = []
for _ in range(m):
    a, b, c = list(map(int, input().split())) # edge (a, b) with length c
    given_vs.append(a)
    possible_vs.append(b)
    g[a].append((b, c)) # stored as (vertex, length)

# Check for sink vertices
for v in possible_vs:
    if v not in given_vs:
        g[v].append((v, 0))

print(g)
print(len(g))

# Look for negative cycles
sol = detect_negative_cycle(g, n, s)
print(sol)