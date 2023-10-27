def build_max_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, len(arr))

def max_heapify(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] < arr[largest]:
        largest = left

    if right < n and arr[right] < arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)

def heap_sort(arr):
    build_max_heap(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)

    return arr

input_arr = [41, 10, 56, 5, 1]
sorted_arr = heap_sort(input_arr)
print(sorted_arr)