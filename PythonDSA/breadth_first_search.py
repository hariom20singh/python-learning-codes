"""
implementation of BFS algorithm.
see: https://en.wikipedia.org/wiki/Breadth-first_search
"""
from typing import Optional, Callable, Any, List

from binary_tree import BinaryTreeNode


def nop(*args, **kwargs):
    pass


def breadth_first_traversal(root: BinaryTreeNode, action: Optional[Callable] = nop):
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
        if action(current_node, queue):
            # if `action` returns a truthy value, it means the traversal is done.
            return True

    return False


def breadth_first_search(root: BinaryTreeNode, value: Any):
    def search_action(current_node: BinaryTreeNode, queue: List):
        if current_node.data == value:
            print(f"{value} was found!")
            return True

        if not queue:
            print(f"{value} was not found.")

    print(f"searching value: {value}")
    return breadth_first_traversal(root=root, action=search_action)


def breadth_first_print(root: BinaryTreeNode, is_print_queue=False):
    def print_action(current_node: BinaryTreeNode, queue: List):
        print(current_node.data)
        if is_print_queue:
            print("queue is:", [node.data for node in queue])

    print(f"printing binary tree from {root.data}:")
    return breadth_first_traversal(root, action=print_action)


def test_stuff():
    # tree looks like this:
    #               1
    #          2         3
    #       4     5   N     6
    #      7 8   N N       N N
    tree = BinaryTreeNode(data=1)
    node2 = tree.left = BinaryTreeNode(data=2)
    node3 = tree.right = BinaryTreeNode(data=3)
    node4 = node2.left = BinaryTreeNode(data=4)
    node2.right = BinaryTreeNode(data=5)
    node3.right = BinaryTreeNode(data=6)
    node4.left = BinaryTreeNode(data=7)
    node4.right = BinaryTreeNode(data=8)

    breadth_first_print(tree)
    print()

    print("bfs 8:")
    assert breadth_first_search(tree, 8)
    print()

    print("bfs 3 8:")
    assert not breadth_first_search(node3, 8)
    print()

    print("bfp queue 4:")
    breadth_first_print(node4, is_print_queue=True)
