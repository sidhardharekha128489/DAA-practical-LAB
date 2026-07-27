import time

# Start execution time
start_time = time.time()

# User input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

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
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

# Display space complexity
print("Space Complexity: O(1)")