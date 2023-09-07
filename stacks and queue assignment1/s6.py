class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def rotate(self):
        temp = self.items[::-1]
        self.items = temp


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.items)
    queue.rotate()
    print(queue.items)


if __name__ == "__main__":
    main()
