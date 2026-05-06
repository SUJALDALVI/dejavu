import heapq

# ---------------------------------
# SELECTION SORT
# ---------------------------------

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # swapping
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ---------------------------------
# PRIM'S ALGORITHM
# ---------------------------------

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

def prims(graph, start):

    visited = []

    min_heap = [(0, start)]

    total_cost = 0

    print("\nPRIM'S ALGORITHM:\n")

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if node not in visited:

            visited.append(node)

            total_cost += weight

            print("Selected Node :", node,
                  "| Cost :", weight)

            for neighbor, edge_weight in graph[node]:

                if neighbor not in visited:
                    heapq.heappush(min_heap,
                                   (edge_weight, neighbor))

    print("\nTotal Minimum Cost =", total_cost)


# ---------------------------------
# KRUSKAL ALGORITHM
# ---------------------------------

edges = [
    ['B', 'C', 1],
    ['A', 'B', 2],
    ['C', 'D', 3],
    ['A', 'C', 4],
    ['B', 'D', 7]
]

def kruskal(edges):

    visited = []

    total_cost = 0

    print("\nKRUSKAL ALGORITHM:\n")

    for edge in edges:

        u = edge[0]
        v = edge[1]
        weight = edge[2]

        # simple cycle checking
        if u not in visited or v not in visited:

            print(u, "-", v,
                  "| Weight =", weight)

            total_cost += weight

            visited.append(u)
            visited.append(v)

    print("\nTotal Minimum Cost =", total_cost)


# ---------------------------------
# MAIN PROGRAM
# ---------------------------------

# SORTING
arr = [64, 25, 12, 22, 11]

print("ORIGINAL ARRAY:")
print(arr)

sorted_array = selection_sort(arr)

print("\nSORTED ARRAY:")
print(sorted_array)


# PRIM'S ALGORITHM
prims(graph, 'A')


# KRUSKAL ALGORITHM
kruskal(edges)