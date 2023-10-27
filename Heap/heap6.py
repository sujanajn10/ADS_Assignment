import heapq

class Task:
    def __init__(self, task_id, priority, execution_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
        self.deadline = deadline

class PriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.time = 0

    def add(self, task):
        heapq.heappush(self.min_heap, (-task.priority, self.time + task.execution_time, task))

    def execute(self):
        while(self.min_heap):
            _, end_time, task = heapq.heappop(self.min_heap)

            if self.time <= task.deadline:
                self.time = end_time
            else:
            
                if not self.min_heap:
                 self.time = 0

pq = PriorityQueue()


t1 = Task(1, 10, 3, 8)
t2 = Task(2, 20, 2, 6)
t3 = Task(3, 30, 1, 5)

pq.add(t1)
pq.add(t2)
pq.add(t3)

pq.execute()