import time

# Start execution time
start_time = time.time()

# User input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    num = int(input())
    arr.append(num)

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# Display the sorted array
print("\nSorted Array:")
for i in range(n):
    print(arr[i], end=" ")

# End execution time
end_time = time.time()

# Display execution time
print("\n\nExecution Time:", end_time - start_time, "seconds")

# Display time complexity
print("Time Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")
print("Space Complexity: O(1)")