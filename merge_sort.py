def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was right
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Testing merge sort
nums = [34, 7, 23, 32, 5, 62]
sorted_nums = merge_sort(nums.copy())
print("Sorted list:", sorted_nums)