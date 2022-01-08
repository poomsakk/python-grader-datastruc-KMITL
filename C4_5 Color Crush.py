class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.insert(0, i)

    def deQueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0


def check(s):
    if len(s) < 3:
        return -1
    for i in range(len(s) - 2):
        if s[i] == s[i+1] == s[i+2]:
            return s[i]
    return -1


# Main
queue = Queue()
ip1, ip2 = input("Enter Input (Normal, Mirror) : ").split()

# enqueue ex in mirr
countMirr = 0
ip2 = ip2[::-1]
while True:
    if check(ip2) == -1:
        break
    ch = check(ip2)
    queue.enQueue(ch)
    ip2 = ip2.replace("{}{}{}".format(ch, ch, ch), "", 1)
    countMirr += 1

# insert from queue
interrupted = 0
while not queue.isEmpty():
    x = queue.deQueue()
    y = check(ip1)
    if y == x:
        interrupted += 1
        ip1 = ip1.replace("{}{}{}".format(x, x, x), x, 1)
    else:
        ip1 = ip1.replace("{}{}{}".format(y, y, y),
                          "{}{}{}{}".format(y, y, x, y), 1)
# explode
countNm = 0
while True:
    if check(ip1) == -1:
        break
    countNm += 1
    ch = check(ip1)
    ip1 = ip1.replace("{}{}{}".format(ch, ch, ch), "", 1)

print("NORMAL :")
print(len(ip1))
print(ip1[::-1]) if not ip1 == "" else print("Empty")
print("{} Explosive(s) ! ! ! (NORMAL)".format(countNm))
if interrupted:
    print("Failed Interrupted {} Bomb(s)".format(interrupted))
print("------------MIRROR------------\n: RORRIM")
print(len(ip2))
print(ip2[::-1]) if not ip2 == "" else print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(countMirr))
