class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.insert(0, i)

    def deQueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
