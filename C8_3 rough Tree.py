from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = Node(0)

    def insert(self, inputList, nodeAmount):    # breadth first search
        queue = deque([])
        queue.append(self.root)
        index = 0
        count = 1
        for i in range(nodeAmount):
            currentNode = queue.popleft()

            if currentNode.left is None:

                if count >= len(inputList) - 1:
                    # insert number in List
                    currentNode.left = Node(inputList[index])
                    index += 1  # insert ... index increasing
                else:
                    # insert Zero (always newNode)
                    currentNode.left = Node(0)

                count += 1  # count every single enQ
                queue.append(currentNode.left)

            if currentNode.right is None:

                if count >= len(inputList) - 1:
                    # insert number in List
                    currentNode.right = Node(inputList[index])
                    index += 1  # insert ... index increasing
                else:
                    # insert Zero (always newNode)
                    currentNode.right = Node(0)

                count += 1  # count every single enQ
                queue.append(currentNode.right)

            if count == nodeAmount:     # complete amount of Node
                break

        return self.root

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level+1)
        print('     '*level, node)
        self.printTree(node.left, level+1)

    def recurNode(self, node):      # depth first search

        if node.left is None and node.right is None:    # check if it is last node
            return node.data                        # return last node data

        left = self.recurNode(node.left)
        right = self.recurNode(node.right)

        if left > right:        # find lessValue
            lessValue = right
        else:
            lessValue = left
        node.data = lessValue   # assign new parent Node

        node.right.data = node.right.data - lessValue   # assign son left
        node.left.data = node.left.data - lessValue     # assign son right
        return lessValue

    def sum(self, node):       # BFS
        count = 0
        if node is None:
            return
        queue = deque([node])
        while len(queue) > 0:
            cur_node = queue.popleft()
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
            count += cur_node.data
        return count


k, inp = input('Enter Input : ').split('/')

k = int(k)
inp = [int(i) for i in inp.split()]

tree = BinarySearchTree()

if len(inp) == k//2+1:
    root = tree.insert(inp, k)          # insert with breadth first search
    tree.recurNode(root)                # recursion of lessValue
    print(tree.sum(root))               # plus every Value in tree
else:
    print('Incorrect Input')
