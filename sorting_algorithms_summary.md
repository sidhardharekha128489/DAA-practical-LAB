# Sorting Algorithms Summary

This markdown document summarizes the sorting scripts present in this workspace.

## Files

- `bubble sort.py`
- `insertion sort.py`
- `merge sort.py`
- `quick sort.py`
- `selection sort.py`

## Overview

Each file is a Python script that:
- reads the number of elements from the user
- reads the list of elements from user input
- sorts the list using one of the five algorithms
- prints the sorted result
- measures and prints execution time
- prints the algorithm's time and space complexity

## Algorithm Summaries

### `bubble sort.py`
- Algorithm: Bubble Sort
- Description: Repeatedly compares adjacent items and swaps them if they are in the wrong order.
- Time Complexity:
  - Best Case: O(n)
  - Average Case: O(n²)
  - Worst Case: O(n²)
- Space Complexity: O(1)

### `insertion sort.py`
- Algorithm: Insertion Sort
- Description: Builds the sorted list one element at a time by inserting each item into its correct position.
- Time Complexity:
  - Best Case: O(n)
  - Average Case: O(n²)
  - Worst Case: O(n²)
- Space Complexity: O(1)

### `merge sort.py`
- Algorithm: Merge Sort
- Description: Recursively divides the list into halves, sorts each half, and merges the sorted halves.
- Time Complexity:
  - Best Case: O(n log n)
  - Average Case: O(n log n)
  - Worst Case: O(n log n)
- Space Complexity: O(n)

### `quick sort.py`
- Algorithm: Quick Sort
- Description: Uses divide and conquer with a pivot element to partition the list and recursively sort partitions.
- Time Complexity:
  - Best Case: O(n log n)
  - Average Case: O(n log n)
  - Worst Case: O(n²)
- Space Complexity: O(log n)

### `selection sort.py`
- Algorithm: Selection Sort
- Description: Repeatedly selects the smallest remaining element and moves it to its final position.
- Time Complexity:
  - Best Case: O(n²)
  - Average Case: O(n²)
  - Worst Case: O(n²)
- Space Complexity: O(1)

## Notes

- All scripts use `time.time()` to record execution duration.
- Input is read from standard input, so they are intended to run interactively.
- The scripts print the sorted array followed by timing and complexity information.
