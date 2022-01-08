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
            elif data >= curNode.data:
                if curNode.right is not None:
                    curNode = curNode.right
                else:
                    curNode.right = Node(data)
                    break
        return self.root

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


tree = BST()
print(" *** Binary Search Tree ***")
ip = [int(i) for i in input('Enter Input : ').split()]
for i in ip:
    root = tree.insert(i)
print("\n --- Tree traversal ---")
print("Level order : ", end="")
tree.BFS(root)
print("\nPreorder : ", end="")
tree.pre_order(root)
print("\nInorder : ", end="")
tree.in_order(root)
print("\nPostorder : ", end="")
tree.post_order(root)
