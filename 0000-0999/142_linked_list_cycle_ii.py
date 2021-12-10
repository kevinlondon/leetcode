# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()

        if not head:
            return
        
        node = head
        while node:
            if id(node) in seen:
                return node
            seen.add(id(node))
            node = node.next
        