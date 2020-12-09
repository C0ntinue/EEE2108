class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        """
        
        :param key: 
        :return: 
        """
        self.__find(self)

    def __find(self, root, key):
        if root.data == key:
            return root
        elif root.data > key:
            return self.__find(root.left, key)
        else:
            return self.__find(root.right, key)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            return self.__insert(self.root, data)

    def __insert(self, node, data):
        if data <= node.data:
            if node.left is not None:
                return self.__insert(node.left, data)
            else:
                node.left = Node(data)
        elif data == node.data:
            print('this data {} is already exist!'.format(data))
            return

        else:  # (data<node.data):
            if node.right is not None:
                return self.__insert(node.right, data)
            else:
                node.right = Node(data)

    def remove(self, value):
        """
        Removes a Node which contains the value `value`.
        To remove a Node, three cases must be handled.
        Case 1: leaf node
                    -> delete it
        Case 2: node has one child
                    -> delete node and put its child in its place
        Case 3: node has two children
                    -> delete node and put its smallest child from its right branch in its place
        """
        if self.root:
            self.root = self.__remove(self.root, value)

    def __remove(self, node, value):
        if node.data == value:

            # Case 1
            if node.left is None and node.right is None:
                return None

            # Case 2
            elif node.left and node.right is None:
                return node.left

            # Case 2
            elif node.left is None and node.right:
                return node.right
            # Case 3
            else:
                parent_node = node
            smallest_node = node.right
            while smallest_node.left:
                parent_node = smallest_node
                smallest_node = smallest_node.left

            # The right Node is the smallest one
            if parent_node == node:
                smallest_node.left = node.left

            # The smallest Node was found to the left of its right branch
            else:
                parent_node.left = smallest_node.right
                smallest_node.left = node.left
                smallest_node.right = node.right
            return smallest_node

        elif node.data > value and node.left:
            node.left = self.__remove(node.left, value)

        elif node.data < value and node.right:
            node.right = self.__remove(node.right, value)

        return node

    def pre_order_traversal(self):
        print()
        self.__pre_order_traversal(self.root)

    def __pre_order_traversal(self, node):
        print(node.data, end=' ')
        if node is None:
            return
        if node.left:
            self.__pre_order_traversal(node.left)
        if node.right:
            self.__pre_order_traversal(node.right)

    def in_order_traversal(self):
        print()
        self.__in_order_traversal(self.root)

    def __in_order_traversal(self, node):

        if node is None:
            return
        if node.left:
            self.__in_order_traversal(node.left)
        print(node.data, end=' ')
        if node.right:
            self.__in_order_traversal(node.right)

    def post_order_traversal(self):
        print()
        self.__post_order_traversal(self.root)

    def __post_order_traversal(self, node):
        if node is None:
            return
        if node.left:
            self.__post_order_traversal(node.left)
        if node.right:
            self.__post_order_traversal(node.right)
        print(node.data, end=' ')


if __name__ == '__main__':

    values = [50, 30, 70, 80, 20, 10, 110, 190, 130, 55]
    t = BinarySearchTree()
    for value in values:
        t.insert(value)

    t.in_order_traversal()
    t.remove(30)
    t.in_order_traversal()
    t.remove(130)
    t.in_order_traversal()

# test
tt=BinarySearchTree()
for value in range(5):
    tt.insert(value)

print(tt.root.data)
print(tt.root.left.data)
