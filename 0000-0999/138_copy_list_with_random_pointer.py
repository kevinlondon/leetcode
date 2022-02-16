"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        while node:
            true_next = node.next
            node.next = Node(node.val, node.next)
            node = true_next

        node = head
        while node:
            if node.random is not None:
                node.next.random = node.random.next

            node = node.next.next

        node = head
        new_head = Node(0)
        last_node = new_head
        while node:
            true_next = node.next.next
            copy = node.next
            last_node.next = copy
            last_node = copy

            node.next = true_next
            node = true_next

        return new_head.next

