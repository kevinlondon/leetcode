"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)

        if not head:
            new_node.next = new_node
            return new_node

        prev = head
        next = head.next
        inserted = False

        while True:
            # insert when -
            # 1. prev <= insertVal <= next
            # 2. insertVal < min (insert at tail)
            # 3. insertVal > max (insert at tail)
            if (prev.val <= insertVal <= next.val or
                insertVal < next.val < prev.val or
                next.val < prev.val < insertVal):
                prev.next = new_node
                new_node.next = next
                inserted = True
                break

            prev = prev.next
            next = next.next
            if prev == head:
                break

        if not inserted:
            prev.next = new_node
            new_node.next = next

        return head
