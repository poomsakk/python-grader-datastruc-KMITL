class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next if next is not None else None
        self.prev = prev if prev is not None else None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev != None:
            s += str(cur.prev.value) + " "
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
        else:
            newNode = Node(item, prev=self.tail)
            self.tail.next = newNode
            self.tail = newNode

    def addHead(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
        else:
            newNode = Node(item, self.head)
            self.head.prev = newNode
            self.head = newNode

    def insert(self, pos, item):
        if pos == 0 or self.isEmpty():
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        elif pos < 0:
            pos = self.size()+pos
            if pos <= 0:
                self.addHead(item)
            else:
                curr = self.nodeAt(pos)
                prev = curr.prev
                newNode = Node(item, curr, prev)
                prev.next = newNode
                curr.prev = newNode
        else:
            curr = self.nodeAt(pos)
            prev = curr.prev
            newNode = Node(item, curr, prev)
            prev.next = newNode
            curr.prev = newNode

    def search(self, item):
        if self.index(item) == -1:
            return "Not Found"
        else:
            return "Found"

    def index(self, item):
        if self.isEmpty():
            return -1
        index = 0
        cur = self.head
        if cur.value == item:
            return index
        while cur.next != None:
            if cur.value == item:
                return index
            index += 1
            cur = cur.next
        return -1

    def size(self):
        if self.isEmpty():
            return 0
        n = 1
        cur = self.head
        while cur.next != None:
            cur = cur.next
            n += 1
        return n

    def pop(self, pos):
        if not 0 <= pos < self.size():
            return "Out of Range"
        if pos == 0:
            nextNode = self.head.next
            self.head.next = None
            self.head = nextNode
            if nextNode is not None:
                nextNode.prev = None
            else:
                self.head = self.tail = None
            return 'Success'
        if pos == self.size() - 1:
            prevNode = self.tail.prev
            self.tail.prev = None
            self.tail = prevNode
            if prevNode is not None:
                prevNode.next = None
            else:
                self.head = self.tail = None
            return 'Success'
        cur = self.nodeAt(pos)
        prevNode = cur.prev
        nextNode = cur.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        cur.prev = None
        cur.next = None
        return 'Success'

    def nodeAt(self, pos):
        cur = self.head
        for _ in range(pos):
            cur = cur.next
        return cur


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
