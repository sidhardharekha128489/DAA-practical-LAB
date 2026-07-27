import time

# Start execution time
start_time = time.time()

# User input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the minimum element with the current element
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

# Display the sorted array
print("\nSorted Array:")
for i in range(n):
    print(arr[i], end=" ")

# End execution time
end_time = time.time()

# Display execution time
print("\n\nExecution Time:", end_time - start_time, "seconds")

# Display time complexity
print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

# Display space complexity
print("Space Complexity: O(1)")