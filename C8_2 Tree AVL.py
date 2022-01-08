class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVL_Tree:
    def insert(self, root, data):
        # function always return root
        # Step 1 - normal recursive insert
        if root is None:
            return Node(data)
        elif data < root.val:
            root.left = self.insert(root.left, data)
        elif data > root.val:
            root.right = self.insert(root.right, data)

        # Step 2 - update height
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - get The Balance (High of L - R)
        balance = self.getBalance(root)

        # Step 4 - if Node isn't balance, Rotate it!

        # Case 1 - Left Left
        if balance > 1 and data < root.left.val:
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and data > root.right.val:
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and data > root.left.val:
            root.left = self.leftRotate(root.left)
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and data < root.right.val:
            root.right = self.rightRotate(root.right)
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)

        return root

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

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)


myTree = AVL_Tree()
root = None

data = [int(x) for x in input("Enter Input : ").split()]
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    myTree.printTree(root)
    print("===============")

# =========================================================================
# a) Left Left Case
# T1, T2, T3 and T4 are subtrees.
#          z                                      y
#         / \                                   /   \
#        y   T4      Right Rotate (z)          x      z
#       / \          - - - - - - - - ->      /  \    /  \
#      x   T3                               T1  T2  T3  T4
#     / \
#   T1   T2
# =========================================================================
# b) Left Right Case
#      z                               z                           x
#     / \                            /   \                        /  \
#    y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
#   / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
# T1   x                          y    T3                    T1  T2 T3  T4
#     / \                        / \
#   T2   T3                    T1   T2
# =========================================================================
# c) Right Right Case
#   z                                y
#  /  \                            /   \
# T1   y     Left Rotate(z)       z      x
#     /  \   - - - - - - - ->    / \    / \
#    T2   x                     T1  T2 T3  T4
#        / \
#      T3  T4
# =========================================================================
# d) Right Left Case
#    z                            z                            x
#   / \                          / \                          /  \
# T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
#     / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
#    x   T4                      T2   y                  T1  T2  T3  T4
#   / \                              /  \
# T2   T3                           T3   T4
# =========================================================================
