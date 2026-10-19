# Travelling Salesman Problem (TSP)

# Distance matrix representing travel costs between cities
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

# Start from city 0
visited = [False] * n
visited[0] = True

path = [0]
best_path = []
minimum_cost = float('inf')


# Generate all possible routes
def tsp(current_city, count, cost):
    global minimum_cost, best_path

    # All cities visited
    if count == n:
        total_cost = cost + graph[current_city][0]

        if total_cost < minimum_cost:
            minimum_cost = total_cost
            best_path = path[:] + [0]

        return

    # Visit unvisited cities
    for next_city in range(n):
        if not visited[next_city]:
            visited[next_city] = True
            path.append(next_city)

            tsp(
                next_city,
                count + 1,
                cost + graph[current_city][next_city]
            )

            # Backtracking
            path.pop()
            visited[next_city] = False


# Solve TSP
tsp(0, 1, 0)

# Display result
print("Travelling Salesman Problem")
print("---------------------------")

print("Minimum Cost Route:", end=" ")

for i in range(len(best_path)):
    print(best_path[i], end="")

    if i < len(best_path) - 1:
        print(" -> ", end="")

print("\nMinimum Travel Cost:", minimum_cost)