# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fake_head, current = ListNode(), head
        fake_head.next = current
        prev_node = fake_head

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next

                prev_node.next = current.next
            else:
                prev_node = current

            current = current.next

        return fake_head.next
