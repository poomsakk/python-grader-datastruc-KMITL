from collections import deque


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

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(str(node)+" ", end="")
        self.in_order(node.right)

    def pre_order(self, node):
        if node is None:
            return
        print(str(node)+" ", end="")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(str(node)+" ", end="")

    def BFS(self, node):
        if node is None:
            return
        queue = deque([node])
        ans = []
        while len(queue) > 0:
            cur_node = queue.popleft()
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
            print(str(cur_node.data) + " ", end="")


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Preorder : ", end="")
T.pre_order(root)
print()
print("Inorder : ", end="")
T.in_order(root)
print()
print("Postorder : ", end="")
T.post_order(root)
print()
print("Breadth : ", end="")
T.BFS(root)
