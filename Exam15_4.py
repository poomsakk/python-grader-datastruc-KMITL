class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            cur_node = self.root
            while True:
                if data < cur_node.data:
                    if cur_node.left is not None:
                        cur_node = cur_node.left
                    else:
                        cur_node.left = Node(data)
                        break
                else:
                    if cur_node.right is not None:
                        cur_node = cur_node.right
                    else:
                        cur_node.right = Node(data)
                        break


def height(obj):
    if obj is None:
        return -1
    else:
        return 1 + max(height(obj.left), height(obj.right))


print(" *** Binary Search Tree Height ***")
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))
for e in arr:
    tree.create(e)
print("Height = ", height(tree.root), end="\n\n")
