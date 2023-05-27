class Stack:
    def __init__(self):
        self.items = []
    def push(self, element):
        self.items.append(element)
    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return None
    def size(self):
        return len(self.items)
    def empty(self):
        return self.size() == 0
    def __str__(self):
        result = '['
        for item in self.items:
            result += str(item) + ' '
        result += ']'
        return result


class newQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def pushright(self, item):
        self.stack1.push(item)
    def popleft(self):
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.empty():
            return None
        else:
            return self.stack2.pop()
    def empty(self):
        return self.stack1.empty() and self.stack2.empty()
    def size(self):
        return self.stack1.size() + self.stack2.size()

def main():
    q = newQueue()
    print(q.empty())  # True

    q.pushright(1)
    q.pushright(2)
    q.pushright(3)

    print(q.empty())  # False
    print(q.size())  # 3

    print(q.popleft())  # 1
    print(q.popleft())  # 2

    q.pushright(4)

    print(q.size())  # 2
    print(q.popleft())  # 3
    print(q.popleft())  # 4
    print(q.empty())  # True

    print(q.popleft())  # None


if __name__ == '__main__':
    main()
