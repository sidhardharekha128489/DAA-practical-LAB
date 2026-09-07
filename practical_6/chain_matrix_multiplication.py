import time

# Matrix Chain Multiplication

# Start execution time
start_time = time.time()

# Number of matrices
n = int(input("Enter the number of matrices: "))

# Store dimensions
# Example: A1 = 10x20, A2 = 20x30, A3 = 30x40
dimensions = []

print("\nEnter dimensions:")
print("For each matrix, enter rows and columns.")

for i in range(n):
    rows = int(input("Enter rows of Matrix " + str(i + 1) + ": "))
    cols = int(input("Enter columns of Matrix " + str(i + 1) + ": "))

    if i > 0 and rows != dimensions[-1]:
        print("Error: Matrix dimensions are not compatible.")
        exit()

    dimensions.append(cols)

# Create dimension array
p = []

# First matrix rows
first_rows = int(input("Enter rows of Matrix 1 again: "))

p.append(first_rows)

for i in range(n):
    p.append(dimensions[i])

# Create cost table
m = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    m.append(row)

# Matrix Chain Multiplication
for length in range(2, n + 1):

    for i in range(n - length + 1):

        j = i + length - 1

        m[i][j] = 999999999

        for k in range(i, j):

            cost = (
                m[i][k]
                + m[k + 1][j]
                + p[i] * p[k + 1] * p[j + 1]
            )

            if cost < m[i][j]:
                m[i][j] = cost

# Minimum multiplication cost
minimum_cost = m[0][n - 1]

# Display result
print("\nMinimum number of scalar multiplications:",
      minimum_cost)

# Display execution time
end_time = time.time()

print("Execution Time:", end_time - start_time, "seconds")

# Complexity
print("\nTime Complexity: O(n^3)")
print("Space Complexity: O(n^2)")