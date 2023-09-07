class FlexiQueue:
    def __init__(self, initial_size=10):
        self.items = []
        self.capacity = initial_size

    def enqueue(self, item):
        if len(self.items) == self.capacity:
            self.items.extend([None] * self.capacity)
            self.capacity *= 2
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
        item = self.items.pop(0)
        if len(self.items) <= self.capacity // 4:
            self.items = self.items[:self.capacity // 2]
            self.capacity //= 2
        return item

    def is_empty(self):
        return len(self.items) == 0


def main():
    queue = FlexiQueue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
