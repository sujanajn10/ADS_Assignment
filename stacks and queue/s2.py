class Queue:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if len(self.items) == self.max_size:
            print("Queue is full")
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


def main():
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    try:
        queue.enqueue(4)
    except Exception as e:
        print(e)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
