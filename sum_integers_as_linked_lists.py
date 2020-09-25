"""
Натуральные числа представлены в виде однонаправленного списка
с цифрами разрядов в значениях от младшего к старшему, например:
    ( 3 -> 2 -> 1 )  # 123 
    ( 2 -> 4 )       # 42

Написать функцию сложения двух чисел, выраженных в виде таких структур.
Например, при сложении списков выше получится:
    ( 5 -> 6 -> 1 )  # 165

"""
from typing import Optional


class Node:
    def __init__(self, value, next_node: Optional['Node'] = None):
        assert value < 10
        self.value = value
        self.next = next_node

    def __iter__(self):
        yield self.value
        next_node = self.next
        while next_node:
            yield next_node.value
            next_node = next_node.next

    def __repr__(self) -> str:
        values = tuple(self)
        representation = ''.join(map(str, reversed(values)))
        return representation


def sum_linked_lists(linked_list_1: Node, linked_list_2: Node) -> Node:
    """
    >>> sum_linked_lists(Node(3, Node(2, Node(1))), Node(2, Node(4)))
    165
    >>> sum_linked_lists(Node(3, Node(2, Node(1))), Node(2, Node(8)))
    205
    >>> sum_linked_lists(Node(3), Node(2))
    5
    >>> sum_linked_lists(Node(3), Node(9))
    12
    >>> sum_linked_lists(Node(3), Node(9, Node(9, Node(9, Node(9)))))
    10002

    """
    sum_values = linked_list_1.value + linked_list_2.value

    value, remainder = sum_values % 10, sum_values // 10
    sum_list = Node(value)
    new_next_node = sum_list

    next_node_1, next_node_2 = linked_list_1.next, linked_list_2.next
    while next_node_1 or next_node_2:

        value_1, value_2 = [getattr(node, 'value', 0) for node in (next_node_1, next_node_2)]
        sum_values = remainder + value_1 + value_2
        value, remainder = sum_values % 10, sum_values // 10

        new_next_node.next = Node(value)

        new_next_node = new_next_node.next
        next_node_1, next_node_2 = [getattr(node, 'next', 0) for node in (next_node_1, next_node_2)]

    if remainder != 0:
        new_next_node.next = Node(remainder)

    return sum_list
