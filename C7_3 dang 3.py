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

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def in_order_traversal(self, node):
        elements = []
        if node.left is not None:
            elements += self.in_order_traversal(node.left)
        elements.append(node.data)
        if node.right is not None:
            elements += self.in_order_traversal(node.right)
        return elements

    def multiple(self, node, n):
        if node is None:
            return
        self.multiple(node.right, n)
        self.multiple(node.left, n)
        if node.data is not None and n < node.data:
            node.data *= 3


T = BST()
data, n = input('Enter Input : ').split("/")
data = data.split()
for i in data:
    root = T.insert(int(i))
T.printTree(root)
print("--------------------------------------------------")
T.multiple(root, int(n))
T.printTree(root)
