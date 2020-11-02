"""
PA4 Prob 1
Justin Huang (jfh5730)
Divyesh Johri (dkj5225)
Eddie Ubri (evu5018)
"""

from collections import defaultdict

# Modified Bellman Ford algorithm with one extra row computation
# Inputs: Graph g = (V, E), n = |V|, s = source vertex
# Outputs: solution dist and calculation of extra row |V|
# Runtime: O(|V|*|E|)
def bellman_ford(g, n, s):

    solRow = []

    # Subproblem dist of size |V|
    # Set dist[s] to 0 and initialize the rest to infinity
    dist = [ float('inf') for _ in range(n) ]
    dist[s-1] = 0

    # Recursively solve the subproblem dist[k]
    for k in range(1, n+1):   # not n, as we need one extra iteration
        for v in g:
            for u, l in g[v]:
                if(dist[v-1] > dist[u-1] + l):
                    dist[v-1] = dist[u-1] + l
        # Save the solution row
        if(k == n-1):
            solRow = dist.copy()

    # Return the extra row and solution row
    return (dist, solRow)


# Algorithm to find negative cycles
# Inputs: Graph g = (V, E), n = |V|, s = source vertex
# Outputs: True -> g has negative cycle
#          False -> g doesn't have a negative cycle
# Runtime: O(|V|*|E|) due to Bellman Ford algorithm
def detect_negative_cycle_bf(g, n, s):

    # Retrieve the extra row and solution row
    dist = bellman_ford(g, n, s)

    if(dist[1] == dist[0]):
        return False
    else:
        return True
    


# Obtain graph information
n, m, s = list(map(int, input().split())) # n vertices, m edges, s = source vertex

# Make the graph
g = defaultdict(list)
for _ in range(m):
    a, b, c = list(map(int, input().split())) # edge (a, b) with length c
    g[a].append((b, c)) # stored as (vertex, length)

# Look for negative cycles
sol = detect_negative_cycle_bf(g, n, s)
print(sol)