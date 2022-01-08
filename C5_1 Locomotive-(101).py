class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Singlylinkedlist:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, item):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)
        self.size += 1

    def popLeft(self):
        data = self.head.next.data
        self.head.next = self.head.next.next
        return data

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Error : out of range")
            return None
        i = 0
        cur = self.head.next
        while True:
            if index == i:
                return cur.data
            else:
                cur = cur.next
                i += 1

    def display(self):
        s = ""
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.next == None:
                s += str(cur.data)
            else:
                s += str(cur.data) + " <- "
        return s


linklist = Singlylinkedlist()
print(" *** Locomotive ***")
ip = input("Enter Input : ").split()
for i in ip:
    linklist.append(i)
print("Before : " + linklist.display())

while linklist.get(0) != '0':
    linklist.append(linklist.popLeft())
print("After : " + linklist.display())
