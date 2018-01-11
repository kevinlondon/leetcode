# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left = right = head
        lead = 0
        traversed = 1
        
        while right.next:
            traversed += 1
            right = right.next
            if lead == n:
                left = left.next
            else:
                lead += 1
             
        if traversed == n:
            return head.next
        else:
            left.next = left.next.next
            return head
            
        