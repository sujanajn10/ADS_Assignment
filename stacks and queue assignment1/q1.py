class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())



