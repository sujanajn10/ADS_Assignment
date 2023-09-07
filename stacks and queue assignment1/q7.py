class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []

    def push(self, url):
        self.back_stack.append(url)

    def pop(self):
        if self.back_stack:
            return self.back_stack.pop()
        else:
            return None

    def forward(self):
        if self.forward_stack:
            return self.forward_stack.pop()
        else:
            return None


def main():
    browser_history = BrowserHistory()
    browser_history.push("https://www.google.com")
    

    print(browser_history.pop())
    print(browser_history.pop())

    print(browser_history.forward())


if __name__ == "__main__":
    main()
