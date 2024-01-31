from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def breadth_first(tree):
    if tree.root is None:
        return []

    output = []
    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        output.append(node.value)

        if node.left is not None:
            queue.enqueue(node.left)

        if node.right is not None:
            queue.enqueue(node.right)

    return output