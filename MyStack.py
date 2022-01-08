class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, n):
        self.items.append(n)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        s = 'stack of ' + str(self.size()) + ' items : '
        for i in self.items:
            s += str(i) + ' '
        return s
