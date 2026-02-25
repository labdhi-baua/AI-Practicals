def is_safe(graph, color, node, c):
    for i in graph[node]:
        if color[i] == c:
            return False
    return True

def graph_coloring_util(graph, n_col, color, node):
    if node == len(graph):
        return True
    for c in range(1, n_col + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if graph_coloring_util(graph, n_col, color, node + 1):
                return True
    return False

def graph_coloring(graph, n_col):
    color = [0] * len(graph)
    if graph_coloring_util(graph, n_col, color, 0):
        return color
    else:
        return False

graph = {0: [1, 2],
         1: [0, 2, 3],
         2: [0, 1, 3],
         3: [1, 2]}
m = 3

coloring = graph_coloring(graph, m)
if coloring:
    print(f"coloring found {coloring}")
else:
    print("coloring not found")