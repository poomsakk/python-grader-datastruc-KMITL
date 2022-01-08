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
        elements = []
        if node.left is not None:
            elements += self.in_order(node.left)
        elements.append(node.data)
        if node.right is not None:
            elements += self.in_order(node.right)
        return elements

    def pre_order(self, node):
        elements = []
        elements.append(node.data)
        if node.left is not None:
            elements += self.pre_order(node.left)
        if node.right is not None:
            elements += self.pre_order(node.right)
        return elements

    def post_order(self, node):
        elements = []
        if node.left is not None:
            elements += self.post_order(node.left)
        if node.right is not None:
            elements += self.post_order(node.right)
        elements.append(node.data)
        return elements

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
            ans.append(cur_node.data)
        return ans

    def findMin(self, node):
        if node.left is None:
            return node.data
        else:
            return self.findMin(node.left)

    def findMax(self, node):
        if node.right is None:
            return node.data
        else:
            return self.findMax(node.right)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print(T.pre_order(root))
print(T.post_order(root))
print(T.in_order(root))
print(T.BFS(root))
print(T.findMax(root))
print(T.findMin(root))
