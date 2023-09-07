class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def findMax(self):
        max_value = None
        for item in self.items:
            if max_value is None or item > max_value:
                max_value = item
        return max_value


def main():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.findMax())


if __name__ == "__main__":
    main()
