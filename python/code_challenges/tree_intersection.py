from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_a, tree_b):
    """
    Finds common value in two binary trees

    Params: binary_tree1, binary_tree2

    Output: Set of common values between the two binary trees
    """

    tree_a_values = set()
    for value in BinaryTree.pre_order(tree_a):
        tree_a_values.add(value)

    tree_b_values = set()
    for value in BinaryTree.pre_order(tree_b):
        if value in tree_a_values:
            tree_b_values.add(value)

    return tree_b_values
