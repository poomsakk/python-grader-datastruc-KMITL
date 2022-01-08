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


inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')

dic = {
    '(': 0,
    '^': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2
}

for i in inp:
    if i not in "()+-*/^":
        print(i, end="")
    elif i in "+-*/^":
        if S.isEmpty():
            S.push(i)
        else:
            while dic.get(i) <= dic.get(S.peek()):
                print(S.pop(), end="")
                if S.isEmpty():
                    break
            S.push(i)
    elif i == '(':
        S.push(i)
    elif i == ')':
        while S.peek() != '(':
            print(S.pop(), end="")
        S.pop()

while not S.isEmpty():
    print(S.pop(), end='')
print()
