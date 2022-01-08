class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, i):
        self.items.insert(0, i)

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)


normalQ = Queue()
extraQ = Queue()
ip = input("Enter Input : ").split(",")
for i in ip:
    if i == 'D':
        if not extraQ.isEmpty():
            print(extraQ.dequeue())
        elif not normalQ.isEmpty():
            print(normalQ.dequeue())
        else:
            print("Empty")
    else:
        a, b = i.split()
        if a == "EN":
            normalQ.enqueue(b)
        elif a == "ES":
            extraQ.enqueue(b)
