from data_structures.kary_tree import KaryTree
from data_structures.queue import Queue


def fizz_buzz_tree(tree):

    if tree.root is None:
        return []

    output = []

    queue = Queue()
    queue.enqueue(tree.root)

    while queue.is_empty():
        node = queue.dequeue()
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3:
            node.value = "Fizz"
        elif node.value % 5:
            node.value = "Buzz"
        else:
            node.value = str(node.value)
        
        output.append(node.value)

    if node.child is not None:
        queue.enqueue(node.child)

    return output
