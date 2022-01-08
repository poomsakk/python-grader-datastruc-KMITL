class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.ans = 0

    def insert(self, data):
        # this method always return root
        if self.root is None:
            self.root = Node(data)
            return self.root
        curNode = self.root
        while True:
            if data < curNode.data:
                if curNode.left is not None:
                    curNode = curNode.left
                else:
                    curNode.left = Node(data)
                    break
            elif data > curNode.data:
                if curNode.right is not None:
                    curNode = curNode.right
                else:
                    curNode.right = Node(data)
                    break
        return self.root

    def DFS(self, node, target, sum):
        if node is None:
            return
        sum += node.data
        if target == sum:
            self.ans += 1
        self.DFS(node.left, target, sum)
        self.DFS(node.right, target, sum)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp, target = input('Enter number / sum : ').split("/")
inp = [int(i) for i in inp.split()]
target = int(target)
for i in inp:
    root = T.insert(i)
T.DFS(root, target, 0)
if T.ans:
    print(f"ANS: {T.ans}")
else:
    print("ANS: NO PATH")
# 5 7 2 4 1/11
# 1 2 3 4 5/6
