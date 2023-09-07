class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) == self.max_size:
            print("Stack is full")
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty")
        return self.items[-1]


def main():
    stack = Stack(3)
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())


if __name__ == "__main__":
    main()
