class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def add(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        root = self.heap.pop(0)
        self.heapify_down(0)

        return root

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def heap_order_property(self):
        for i in range(len(self.heap)):
            if (self.left(i) < len(self.heap) and self.heap[i] < self.heap[self.left(i)]) or (self.right(i) < len(self.heap) and self.heap[i] < self.heap[self.right(i)]):
                return False
        return True