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
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, element):
        self.items.append(element)
    def dequeue(self):
        if not self.empty():
            return self.items.pop(0)
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

def main():
    s = Stack()  
    print(s)  
    print(s.empty())  
    s.push(1)
    s.push(4)
    s.push(5)
    print(s)  
    print(s.size())  
    print(s.empty())  
    x = s.pop()
    print(x)  
    print(s)  
    s.pop()
    s.pop()  
    x = s.pop()
    print(x)  
    print('-'*40)
    print("the QUEUE")
    q = Queue()  
    print(q)  
    print(q.empty())  
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(5)
    print(q)  
    print(q.size())  
    print(q.empty())  
    x = q.dequeue()
    print(x)  
    print(q)  
    q.dequeue()
    q.dequeue()  
    x = q.dequeue()
    print(x)  


if __name__ == '__main__':
    main()