from collections import deque


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = deque()
        else:
            self.items = deque(list)

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0


activity = {
    '0': "Eat",
    '1': "Game",
    '2': "Learn",
    '3': "Movie"
}
location = {
    '0': "Res.",
    '1': "ClassR.",
    '2': "SuperM.",
    '3': "Home"
}

myQ = Queue()
myQ2 = Queue()
youQ = Queue()
youQ2 = Queue()
score = 0
ip = input("Enter Input : ").split(",")
for day in ip:
    m, y = day.split()
    myQ.enQueue(m)
    youQ.enQueue(y)

print("My   Queue = ", end="")
while not myQ.isEmpty():
    x = myQ.deQueue()
    print(x, end="")
    myQ2.enQueue(x)
    if not myQ.isEmpty():
        print(", ", end="")
print()

print("Your Queue = ", end="")
while not youQ.isEmpty():
    x = youQ.deQueue()
    print(x, end="")
    youQ2.enQueue(x)
    if not youQ.isEmpty():
        print(", ", end="")
print()

print("My   Activity:Location = ", end="")
while not myQ2.isEmpty():
    x = myQ2.deQueue()
    myQ.enQueue(x)
    myAc, myLo = x.split(":")
    print("{}:{}".format(activity[myAc], location[myLo]), end="")
    if not myQ2.isEmpty():
        print(", ", end="")
print()

print("Your Activity:Location = ", end="")
while not youQ2.isEmpty():
    x = youQ2.deQueue()
    youQ.enQueue(x)
    youAc, youLo = x.split(":")
    print("{}:{}".format(activity[youAc], location[youLo]), end="")
    if not youQ2.isEmpty():
        print(", ", end="")
print()

# calculate score
while not myQ.isEmpty():
    myAc, myLo = myQ.deQueue().split(":")
    youAc, youLo = youQ.deQueue().split(":")
    if myAc == youAc and myLo != youLo:
        score += 1
    elif myAc != youAc and myLo == youLo:
        score += 2
    elif myAc == youAc and myLo == youLo:
        score += 4
    elif myAc != youAc and myLo != youLo:
        score -= 5
if score >= 7:
    print("Yes! You're my love! : Score is {}.".format(score))
elif score > 0:
    print("Umm.. It's complicated relationship! : Score is {}.".format(score))
else:
    print("No! We're just friends. : Score is {}.".format(score))
