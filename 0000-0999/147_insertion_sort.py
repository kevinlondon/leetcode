import py.test
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        tail = head.next

        while tail:
            node = tail
            tail = tail.next

            if node.val < head.val:
                node.next = head
                head = node
                continue

            last_node = head
            next_node = head.next
            while next_node and next_node != tail:
                if node.val < next_node.val:
                    last_node.next = node
                    node.next = next_node
                    break
                else:
                    last_node = node
                    next_node = node.next

        return head
