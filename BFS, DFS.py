#BFS
def bfs(graph, start_node):
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=' ')

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph = {'1':['2', '3'],
         '2':['4','5'],
         '3':['6'],
         '4':[],
         '5':['6'],
         '6':[]}
bfs(graph,'1')

print()
#DFS
def dfs(graph, start_node):
    visited = []
    stack = []
    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.append(current_node)
            for neighbour in reversed(graph[current_node]):
                if neighbour not in visited:
                    stack.append(neighbour)


graph = {'1': ['2', '3'],
         '2': ['4', '5'],
         '3': ['6'],
         '4': [],
         '5': ['6'],
         '6': []}
dfs(graph, '1')