# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    """
    Approach:
        Have two pointers walking to and from the tail.
        We can't get "next" but we could keep a stack from which we pop
        Then we walk the pointers in each direction until we intercept
        What if we pass each other since they're both moving?
        Maybe we track the length traversed as well.

        Alternatively, if we keep a deque, we could pop last and first and
        just get the middle elements.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        current_node = head.next
        list_contents = deque()

        while current_node:
            list_contents.append(current_node)
            current_node = current_node.next

        last_popped_right = True
        if list_contents:
            current_node = list_contents.pop()
            head.next = current_node

        while list_contents:
            if last_popped_right:
                next_node = list_contents.popleft()
            else:
                next_node = list_contents.pop()

            last_popped_right = not last_popped_right

            current_node.next = next_node
            next_node.next = None
            current_node = next_node

        return head

