#bfs
def bfs(graph, start_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end = " ")
        visited.append(current_node)

        for neighbours in graph[current_node]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)

bfs(graph = {'1': ['2', '4'],
             '2': ['3', '5'],
             '3': [],
             '4': ['6'],
             '5': ['6'],
             '6': ['7'],
             '7': []}, start_node = '1')

#dfs
def dfs(graph, start_node):
    visited = []
    stack = []

    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node, end = " ")
            visited.append(current_node)

            for neighbours in reversed(graph[current_node]):
                if neighbours not in visited:
                    stack.append(neighbours)

dfs(graph = {
    '1': ['2', '4'],
    '2': ['3', '5'],
    '3': [],
    '4': ['6'],
    '5': ['6'],
    '6': ['7'],
    '7': []}, start_node = '1')





















        
