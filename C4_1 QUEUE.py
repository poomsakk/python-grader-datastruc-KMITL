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


q = Queue()
ip = input("Enter Input : ").split(",")
for i in ip:
    if i == 'D':
        if q.isEmpty():
            print("-1")
        else:
            print("{} 0".format(q.dequeue()))
    else:
        a, b = i.split()
        q.enqueue(b)
        print(q.size())
if q.isEmpty():
    print("Empty")
else:
    while not q.isEmpty():
        print("{} ".format(q.dequeue()), end="")
