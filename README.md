# geeksforgeeks-merge-sort
Here’s a simple README.md file for the geeksforgeeks-merge-sort GitHub repository:

# Merge Sort Algorithm

This repository provides a Python implementation of the Merge Sort algorithm, a powerful, stable sorting technique with a time complexity of **O(n log n)**. Merge Sort is ideal for sorting large datasets where consistent, efficient sorting is needed. The code is well-documented for easy understanding.

## Table of Contents
- [Introduction](#introduction)
- [How Merge Sort Works](#how-merge-sort-works)
- [Code](#code)
- [Usage](#usage)
- [Advantages of Merge Sort](#advantages-of-merge-sort)
- [Comparison with Other Algorithms](#comparison-with-other-algorithms)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Merge Sort is a divide-and-conquer algorithm that splits an array into halves, recursively sorts each half, and then merges them back into a single sorted array. It consistently performs in **O(n log n)** time, making it one of the fastest general-purpose sorting algorithms.

## How Merge Sort Works

1. **Divide**: Split the array into two halves until each subarray contains a single element.
2. **Conquer**: Recursively sort each half.
3. **Combine**: Merge the sorted halves back into one sorted array.

## Code

Here's the main Merge Sort function:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

Usage

To use this code, simply import or paste the merge_sort function into your project, and call it with an unsorted array.

Example:

arr = [34, 7, 23, 32, 5, 62]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

Advantages of Merge Sort

	•	Efficiency: Consistently performs in O(n log n) time.
	•	Stability: Maintains the relative order of equal elements.
	•	Predictable Performance: Suitable for large datasets without degrading to O(n²).


Contributing

Feel free to fork this repository, submit issues, or make pull requests to improve the implementation or documentation.
