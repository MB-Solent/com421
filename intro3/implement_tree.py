class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_node):
        if new_node.value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(new_node)
        elif new_node.value > self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(new_node)
        else:
            print("Value is not unique in the tree.")


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, *args):
        for value in args:
            if self.root is None:
                self.root = TreeNode(value)
            else:
                self.root.insert(TreeNode(value))

    def recursive_print(self, current_node=None):
        if self.root is not None:
            if current_node is None:
                current_node = self.root

            if current_node.left is not None:
                self.recursive_print(current_node.left)
            print(current_node.value)
            if current_node.right is not None:
                self.recursive_print(current_node.right)

        else:
            print("Tree is empty.")


tree = BinaryTree()

tree.add(5)

tree.add(2)

tree.add(6)

tree.add(3, 4, 20, 15)

tree.recursive_print()

