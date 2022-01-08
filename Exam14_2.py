from collections import deque


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = deque()
        else:
            self.items = deque(list)

    def __str__(self):
        if self.isEmpty():
            return "Empty Queue"
        s = "Queue data : "
        for i in self.items:
            s = s + str(i) + " "
        return s

    def __len__(self):
        return len(self.items)

    def enQueue(self, data):
        self.items.append(data)

    def deQueue(self):
        return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0


choice = int(input("Enter choice : "))
if choice == 1:
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :", len(q1))
    print(q1)
elif choice == 2:
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :", q1.isEmpty())
elif choice == 3:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :", len(q1))
    print("Queue is Empty :", q1.isEmpty())
