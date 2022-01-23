# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head, node = None, None

        i, j = list1, list2
        while i or j:
            a = i.val if i else float('inf')
            b = j.val if j else float('inf')

            if (i and not j) or a < b:
                next_node = i
                i = i.next
            else:
                next_node = j
                j = j.next

            if not node:
                merged_head = next_node
            else:
                node.next = next_node

            node = next_node

        return merged_head
