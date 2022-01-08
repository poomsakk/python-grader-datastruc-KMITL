class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

        def __str__(self):
            return str(self.data)

    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        s = ""
        p = self.head
        while p != None:
            s += str(p.data)
            p = p.next
            if p != None:
                s += ' <- '
        return s

    def __len__(self):
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail = p
        self.size += 1

    def removeHead(self):
        if self.head == None:
            return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p

    def calculate(self):
        h = self.head
        if h.data == 0:
            return
        t = self.nodeAt(self.size - 1)
        prev = self.head
        for i in range(self.size):
            node = self.nodeAt(i)
            if node.data == 0:
                prev = self.nodeAt(i-1)
                break
        prev.next = None
        t.next = h
        self.head = node


print(" *** Re order ***")
ip = [int(x) for x in input("Enter Input : ").split()]
l = LinkedList()
for i in ip:
    l.append(i)
print(f"Before : {l}")
l.calculate()
print(f"After : {l}")
