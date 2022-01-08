class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return


def createList(l=[]):
    cur = head = node(None)
    for i in l:
        cur.next = node(i)
        cur = cur.next
    return head


def printList(H):
    cur = H
    s = ""
    while cur.next != None:
        s += str(cur.next.data) + " "
        cur = cur.next
    print(s)


def mergeOrderesList(p, q):
    current_p = p.next
    current_q = q.next
    cur = head = node(None)
    while current_p != None or current_q != None:
        if current_p == None:
            cur.next = current_q
            break
        elif current_q == None:
            cur.next = current_p
            break
        if current_p.data <= current_q.data:
            cur.next = current_p
            current_p = current_p.next
            cur = cur.next
        else:
            cur.next = current_q
            current_q = current_q.next
            cur = cur.next
    return head


#################### FIX comand ####################
# input only a number save in L1,L2
ip1, ip2 = input("Enter 2 Lists : ").split()
L1 = [int(x) for x in ip1.split(",")]
L2 = [int(x) for x in ip2.split(",")]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)
