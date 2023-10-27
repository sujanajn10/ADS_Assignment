class Task:
    def __init__(self, task_id, priority, execution_time):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time

def compute_schedule(tasks):
    tasks = sorted(tasks, key=lambda x: (-x.priority, x.execution_time))
    current_time = 0
    waiting_time = [0] * len(tasks)
    turnaround_time = [0] * len(tasks)

    for i in range(len(tasks)):
        task = tasks[i]
        current_time += task.execution_time
        waiting_time[i] = current_time - task.execution_time
        turnaround_time[i] = current_time - task.execution_time

    return waiting_time, turnaround_time

tasks = [
    Task(1, 5, 10),
    Task(2, 8, 20),
    Task(3, 3, 5),
    Task(4, 10, 30),
    Task(5, 1, 2)
]

waiting_time, turnaround_time = compute_schedule(tasks)

print("Waiting Time: ", waiting_time)
print("Turnaround Time: ", turnaround_time)