"""
PA5 Prob 2
Justin Huang (jfh5730)
Divyesh Johri (dkj5225)
Eddie Ubri (evu5018)
"""

from functools import reduce

class Node:
    def __init__(self, vertex):
        self.data = vertex
        self.height = 0
        self.parent = None

class Solution:

    # Initializes a tree
    # INPUT: Node object x
    def make_set(self, x):
        x.height = 1
        x.parent = x
    
    # Finds root of tree node is located in
    # INPUT: Node object x
    # OUTPUT: Root of x
    def find(self, x):
        while( x.parent != x):
            x = x.parent        
        return x

    # Union will combine two trees so the smaller height tree is connected to the larger tree
    # INPUT: Node objects x and y (separate trees)    
    def union(self, x, y):

        # Find roots of 
        rx = self.find(x)
        ry = self.find(y)
        # If roots are the same, then they are already in the same tree
        if( rx == ry ):
            return
        
        if( rx.height < ry.height ):
            rx.parent = ry           
        elif ( ry.height < rx.height ):
            ry.parent = rx
        else:
            rx.parent = ry
            ry.height =+ 1

    # Gets weight of edge
    # INPUT: edge tuple
    # OUPUT: weight of tuple
    def weight(self, edge):
        return edge[2]


    # Will find edge length of the minimum spanning tree of the given graph
    # INPUT: V vertices, E edges
    # OUTPUT: edge length of minimum spanning tree
    def kruskal(self, V, E):
        
        # Sort edges
        E.sort(key=self.weight)

        # Initialize new edge set
        E1 = []

        # Make trees based on graph vertices
        for v in range(len(V)):
            node = Node(V[v])
            self.make_set(node)      
            V[v] = node
            
        # Loop through e = (u,v) in Edges
        for e in E:            
            u = None
            v = None

            # Get nodes
            for node in range(len(V)):
                if V[node].data == e[0]:
                    u = node
                if V[node].data == e[1]:
                    v = node
            
            if not u and not v:
                return "error: unrecognized vertices in edges"

            # Get roots of nodes
            ru = self.find(V[u])
            rv = self.find(V[v])

            if ru != rv:
                E1.append(e[2])
                self.union(ru, rv)
        
        return reduce( lambda x,y: x + y, E1 )

                   




# Obtain graph information
n, m = list(map(int, input().split())) # n vertices, m edges

# Make the graph
E = []
V = []
for _ in range(m):
    a, b, c = list(map(int, input().split())) # edge (a, b) with weight c

    if a not in V:
        V.append(a)    
    if b not in V:
        V.append(b)

    E.append((a, b, c)) # stored as (vertex, vertex, weight)


sol = Solution()
print(sol.kruskal(V, E))