import collections

# ==================================================
# DFS (Depth First Search)
# ==================================================

graph_dfs = {
    'A': ['B', 'C', 'D'],
    'B': [],
    'C': ['E', 'D'],
    'D': [],
    'E': []
}

visited = set()

print("\n========== DFS ALGORITHM ==========\n")

print("Graph:\n")

print("""
        A
      / | \\
     B  C--D
        |
        E
""")

print("Graph Connections:")
print("A -> B, C, D")
print("C -> E, D")

print("\nDFS Traversal:\n")


# DFS FUNCTION
def dfs(visited, graph, node):

    if node not in visited:

        print(node)

        visited.add(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# CALL DFS
dfs(visited, graph_dfs, 'A')


# ==================================================
# BFS (Breadth First Search)
# ==================================================

graph_bfs = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]
}

print("\n========== BFS ALGORITHM ==========\n")

print("Graph:\n")

print("""
          0
        / | \\
       1--2  3
           |
           4
""")

print("Graph Connections:")
print("0 -> 1, 2, 3")
print("1 -> 0, 2")
print("2 -> 0, 1, 4")
print("3 -> 0")
print("4 -> 2")

print("\nBFS Traversal:\n")


# BFS FUNCTION
def bfs(graph, start):

    visited = set([start])

    queue = collections.deque([start])

    while queue:

        vertex = queue.popleft()

        print(vertex)

        for neighbour in graph[vertex]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(neighbour)


# CALL BFS
bfs(graph_bfs, 0)