# Floyd-Warshall Algorithm

INF = 99999

# Graph represented as an adjacency matrix
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(graph)

# Copy the graph manually
dist = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(graph[i][j])
    dist.append(row)

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                new_distance = dist[i][k] + dist[k][j]

                if new_distance < dist[i][j]:
                    dist[i][j] = new_distance

# Display shortest distance matrix
print("Shortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print("INF", end="\t")
        else:
            print(dist[i][j], end="\t")
    print()