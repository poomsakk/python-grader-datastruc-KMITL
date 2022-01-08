class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Singlylinkedlist:
    def __init__(self, lis=None):
        self.head = Node()
        self.size = 0
        if lis != None:
            for i in lis:
                self.append(i)

    def append(self, item):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)
        self.size += 1

    def appendLeft(self, n):
        if self.isEmpty():
            self.head.next = Node(n)
        else:
            sec = self.head.next
            self.head.next = Node(n)
            self.head.next.next = sec
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Empty!!")
            return
        prevNode = cur = self.head
        while cur.next != None:
            prevNode = cur
            cur = cur.next
        prevNode.next = None
        self.size -= 1
        return cur.data

    def popLeft(self):
        data = self.head.next.data
        if self.size == 1:
            self.head.next = None
        else:
            self.head.next = self.head.next.next
        self.size -= 1
        return data

    def isEmpty(self):
        return self.size == 0

    def clear(self):
        self.head.next = None
        self.size = 0

    def rdSort(self):
        pos = Singlylinkedlist()
        neg = Singlylinkedlist()
        while not self.isEmpty():
            item = self.popLeft()
            pos.append(item) if item >= 0 else neg.append(item)
        digit = [Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(
        ), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist()]
        # positive sort
        maxdigit = pos.__maxDigit()
        for i in range(0, maxdigit+1):
            while not pos.isEmpty():
                n = pos.popLeft()
                d = pos.__getdigit(n, i)
                digit[d].appendLeft(n)
            for j in range(9, -1, -1):
                while not digit[j].isEmpty():
                    x = digit[j].popLeft()
                    pos.appendLeft(x)
            if not digit[0].isEmpty() and digit[1].isEmpty() and digit[2].isEmpty() and digit[3].isEmpty() and digit[4].isEmpty() and digit[5].isEmpty() and digit[6].isEmpty() and digit[7].isEmpty() and digit[8].isEmpty() and digit[9].isEmpty():
                break
        # negative sort
        maxdigit = neg.__maxDigit()
        for i in range(0, maxdigit+1):
            while not neg.isEmpty():
                n = neg.popLeft()
                d = neg.__getdigit(n, i)
                digit[d].appendLeft(n)
            for j in range(9, -1, -1):
                while not digit[j].isEmpty():
                    x = digit[j].popLeft()
                    neg.appendLeft(x)
            if not digit[0].isEmpty() and digit[1].isEmpty() and digit[2].isEmpty() and digit[3].isEmpty() and digit[4].isEmpty() and digit[5].isEmpty() and digit[6].isEmpty() and digit[7].isEmpty() and digit[8].isEmpty() and digit[9].isEmpty():
                break
        while not pos.isEmpty():
            self.append(pos.pop())
        while not neg.isEmpty():
            self.append(neg.popLeft())

    def display(self):
        cur = self.head
        print("DATA = ", end="")
        while cur.next != None:
            cur = cur.next
            print("{} ".format(cur.data), end="")

    def radixSort(self):
        bfStr = ""
        cur = self.head
        while cur.next != None:
            cur = cur.next
            bfStr += "{}".format(cur.data)
            bfStr += " -> " if cur.next != None else ""
        round = 1
        digit = [Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(
        ), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist(), Singlylinkedlist()]
        maxdigit = self.__maxDigit()
        for i in range(0, maxdigit+1):
            print("------------------------------------------------------------")
            print("Round : {}".format(round))
            round += 1
            while not self.isEmpty():
                n = self.popLeft()
                d = self.__getdigit(n, i)
                digit[d].appendLeft(n) if n >= 0 else digit[d].append(n)
            for j in range(10):
                digit[j].rdSort()
                print("{} : ".format(j), end="")
                cur = digit[j].head
                while cur.next != None:
                    cur = cur.next
                    print("{} ".format(cur.data), end="")
                print()
            if not digit[0].isEmpty() and digit[1].isEmpty() and digit[2].isEmpty() and digit[3].isEmpty() and digit[4].isEmpty() and digit[5].isEmpty() and digit[6].isEmpty() and digit[7].isEmpty() and digit[8].isEmpty() and digit[9].isEmpty():
                break
            for j in range(9, -1, -1):
                while not digit[j].isEmpty():
                    x = digit[j].popLeft()
                    self.appendLeft(x)
        afStr = ""
        cur = digit[0].head
        while not digit[0].isEmpty():
            x = digit[0].popLeft()
            self.append(x)
            afStr += "{}".format(x)
            afStr += " -> " if not digit[0].isEmpty() else ""
        print("------------------------------------------------------------")
        print("{} Time(s)".format(round-2))
        print("Before Radix Sort : {}".format(bfStr))
        print("After  Radix Sort : {}".format(afStr))

    def __getdigit(self, num, pos):
        return (abs(num)//(10**pos)) % 10

    def __maxDigit(self):
        cur = self.head
        maxx = 0
        while cur.next != None:
            cur = cur.next
            num = abs(cur.data)
            i = 0
            while num != 0:
                num //= 10
                i += 1
            maxx = max(i, maxx)
        return maxx


ip = [int(x) for x in input("Enter Input : ").split()]
linklist = Singlylinkedlist(ip)
linklist.radixSort()
