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

    def getNode(self, index):
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur

    def display(self):
        if self.size == 0:
            print("Empty")
            return
        s = ""
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.next == None:
                s += str(cur.data)
            else:
                s += str(cur.data) + "->"
        print(s)

    def detectLoop(self):
        s = set()
        cur = self.head
        while cur.next != None:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        return False


L = Singlylinkedlist()
ip = input("Enter input : ").split(",")
loop = False
for i in ip:
    if i[:1] == "A":
        L.append(int(i[2:]))
        L.display()
    elif i[:1] == "S":
        a, b = i[2:].split(":")
        a = int(a)
        b = int(b)
        len = L.size
        if len == 0:
            print("Error! "+"{"+"list is empty"+"}")
        elif a > len-1 and 0 <= b < len:  # a out of range, b in range
            print("Error! "+"{"+"index not in length"+"}"+": {}".format(a))
        elif 0 <= a < len and b > len-1:  # b out of range, a in range
            print("index not in length, append : {}".format(b))
            L.append(b)
        elif 0 <= a < len and 0 <= b < len:  # both in range
            node_a = L.getNode(a)
            node_b = L.getNode(b)
            node_a.next = node_b
            print("Set node.next complete!, index:value = {}:{} -> {}:{}".format(a,
                  node_a.data, b, node_b.data))
if L.detectLoop():
    print("Found Loop")
else:
    print("No Loop")
    L.display()
