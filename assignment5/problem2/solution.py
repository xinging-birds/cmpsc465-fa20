class Node:

    def __init__(data):
        self.data = data
        self.height = 0
        self.parent = None

class DisjointSet:

    def __init__(self, roots):
        for root in roots:
            self.make_set(root)

    def make_set(x):

