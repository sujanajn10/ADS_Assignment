class Task:
    def __init__(self, task_id, priority, execution_time):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert_key(self, k):
        heappush(self.heap, k)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)

class PriorityQueue:
    def __init__(self):
        self.min_heap = MinHeap()
        self.time = 0

    def add(self, task):
        self.min_heap.insert_key((task.priority, self.time + task.execution_time, task))

    def execute(self):
        waiting_time = {}
        turnaround_time = {}

        while(not self.min_heap.is_empty()):
            _, end_time, task = heappop(self.min_heap.heap)
            self.time = end_time

            if task.task_id in waiting_time:
                waiting_time[task.task_id] += self.time - waiting_time[task.task_id] - task.execution_