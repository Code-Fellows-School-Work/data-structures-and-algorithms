import pytest
from data_structures.linked_list import LinkedList

def test_exists():
    assert LinkedList

# Used ChatGPT to write test code
def test_append():
    linked = LinkedList()
    linked.append(1)
    assert linked.head.value == 1

def test_append_multiple_nodes():
    linked = LinkedList()
    values_to_append = [1, 2, 3, 4, 5]

    for value in values_to_append:
        linked.append(value)

    current = linked.head
    for value in values_to_append:
        assert current.value == value
        current = current.next
        
def test_insert_before_middle():
    linked = LinkedList()
    values_to_insert = [1, 2, 4, 5]
    target = 4
    new_value = 3

    for value in values_to_insert:
        linked.append(value)

    linked.insert_before(target, new_value)

    expected_values = [1, 2, 3, 4, 5]
    current = linked.head

    for value in expected_values:
        assert current.value == value
        current = current.next