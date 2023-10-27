class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_max(self):
        if not self.is_empty():
            return self.heap[0]

    def extract_max(self):
        if not self.is_empty():
            max_value = self.heap[0]
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap.pop()
            self.max_heapify(0)
            return max_value

    def add(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def max_heapify(self, index):
        left = self.left_child_index(index)
        right = self.right_child_index(index)
        largest = index

        if left < self.size() and self.heap[left] > self.heap[largest]:
            largest = left

        if right < self.size() and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.max_heapify(largest)

    def heapify_up(self, index):
        parent = self.parent_index(index)
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.swap(parent, index)
            self.heapify_up(parent)

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return index * 2 + 1

    def right_child_index(self, index):
        return index * 2 + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def check_max_heap_property(max_heap):
    for i in range(max_heap.size()):
        left = max_heap.left_child_index(i)
        right = max_heap.right_child_index(i)

        if left < max_heap.size() and max_heap.heap[i] < max_heap.heap[left]:
            return False

        if right < max_heap.size() and max_heap.heap[i] < max_heap.heap[right]:
            return False

    return True