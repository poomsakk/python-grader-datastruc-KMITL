class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


S = Stack()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i != 'B':
        a, b = i.split()
        if S.isEmpty():
            S.push(int(b))
        else:
            if int(b) < S.peek():
                S.push(int(b))
            else:
                while int(b) > S.peek():
                    S.pop()
                    if S.isEmpty():
                        break
                if S.isEmpty():
                    S.push(int(b))
                    continue
                if S.peek() > int(b):
                    S.push(int(b))
        # print(S.items)
    else:
        print(S.size())
