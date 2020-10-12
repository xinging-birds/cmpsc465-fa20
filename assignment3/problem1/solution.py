from collections import defaultdict

# Problem Number One
# Macbook > Anything else

first, second = list(map(int, input().split()))

graph = defaultdict(list)

def DFS(graph, number, node, stack):
    node[number] = 1

    for i in graph[number]:
        if not node[i]:
            DFS(graph, i, node, stack)
    stack.append(number)


def CheckerDFS(graph, number, node):
    node[number] = 1

    for i in graph[number]:
        if not node[i]:
            CheckerDFS(graph, i, node)



def x(graph, variable):
    x = 0
    master_stack = []
    been_to = [False] * (variable + 1)
    node_checker = (variable + 1) * [False]
    inverse_graph = transpos(graph, variable)

    for i in range(1, variable + 1):
        if not been_to[i]:
            DFS(graph, i, been_to, master_stack)

    while (master_stack).__len__() != 0:
        top_of_stack = master_stack.pop()
        if not node_checker[top_of_stack]:
            x += 1
            CheckerDFS(inverse_graph, top_of_stack, node_checker)
    return x


def transpos(graph, var):
    transpos_graph = defaultdict(list)

    for i in range(1, var + 1):
        for k in graph[i]:
            transpos_graph[k].append(i)
    return transpos_graph


for i in range(second):
    third, fourth = list(map(int, input().split()))
    graph[third].append(fourth)

print(x(graph, first))

