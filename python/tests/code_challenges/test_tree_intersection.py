import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    # corrected the array of values to match the code challenge
    values = [42, 100, 600, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    # corrected the output to match the code challenge output
    expected = [100, 160, 125, 175, 200, 350, 500]

    assert sorted(actual) == sorted(expected)


def test_tree_intersection_two():

    tree_a = BinaryTree()
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    # corrected the array of values to match the code challenge
    values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    # corrected the output to match the code challenge output
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    assert sorted(actual) == sorted(expected)

def test_tree_intersection_three():

    tree_a = BinaryTree()
    values = ["red", "blue", "green"]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    # corrected the array of values to match the code challenge
    values = ["orange", "red", "yellow"]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    # corrected the output to match the code challenge output
    expected = ["red"]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
