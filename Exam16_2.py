class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert2(self.root, data)

    def insert2(self, node, data):
        if node is None:
            return Node(data)
        elif data < node.val:
            node.left = self.insert2(node.left, data)
        elif data > node.val:
            node.right = self.insert2(node.right, data)
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        balance = self.getBalance(node)
        if balance > 1 and data < node.left.val:
            return self.rightRotate(node)
        if balance < -1 and data > node.right.val:
            return self.leftRotate(node)
        if balance > 1 and data > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and data < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        self.root = node
        return node

    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def getBalance(self, root):
        if root is None:
            return 0
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def print_inorder(self, node):
        if node is None:
            return
        self.print_inorder(node.left)
        print(f"{node} ", end="")
        self.print_inorder(node.right)

    def print_preorder(self, node):
        if node is None:
            return
        print(f"{node} ", end="")
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def print_postorder(self, node):
        if node is None:
            return
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(f"{node} ", end="")

    def inorder(self):
        print("in_order  --> ", end="")
        self.print_inorder(self.root)
        print()

    def preorder(self):
        print("preorder  --> ", end="")
        self.print_preorder(self.root)
        print()

    def postorder(self):
        print("postorder --> ", end="")
        self.print_postorder(self.root)
        print()


print(" *** AVL Tree ***")
input_string = input("Enter some numbers : ")
bst = AVLTree()
for n in input_string.split():
    bst.insert(int(n))
bst.inorder()
bst.preorder()
bst.postorder()
