# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = current = ListNode()

        queue = PriorityQueue()

        for idx, head in enumerate(lists):
            if head:
                queue.put((head.val, idx, head))

        while not queue.empty():
            _, idx, node = queue.get()
            current.next = node
            if node.next:
                queue.put((node.next.val, idx, node.next))
            current = node

        return dummy.next
