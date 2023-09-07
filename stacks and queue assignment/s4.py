class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, item):
        self.q1.append(item)

    def pop(self):
        if len(self.q2) == 0:
            while len(self.q1) > 0:
                self.q2.append(self.q1.pop(0))
        return self.q2.pop(0)

    def is_empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0


def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
