import time

# Find the parent of a vertex
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


# Union of two sets
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Sort edges by weight without using sort() or sorted()
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if edges[i][2] > edges[j][2]:
                edges[i], edges[j] = edges[j], edges[i]

    parent = list(range(vertices))
    rank = [0] * vertices

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == vertices - 1:
                break

    if len(mst) != vertices - 1:
        print("MST cannot be formed: Graph is disconnected.")
        return

    print("\nEdges in Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} : {weight}")

    print("Total MST Cost:", total_cost)


# Main Program
vertices = int(input("Enter number of vertices: "))
edges_count = int(input("Enter number of edges: "))

edges = []

print("Enter each edge as: source destination weight")
print(f"Use vertex numbers from 0 to {vertices - 1}.")

for i in range(edges_count):
    u, v, weight = map(
        int, input(f"Edge {i + 1}: ").split()
    )
    edges.append((u, v, weight))

# Measure algorithm execution time only
start_time = time.perf_counter()

kruskal(vertices, edges)

end_time = time.perf_counter()

print("\nExecution Time:", end_time - start_time, "seconds")
print("Time Complexity: O(E log E)")
print("Space Complexity: O(V + E)")