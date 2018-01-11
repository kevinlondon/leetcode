# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        previous_node = None
        carry = 0
        first_node = None

        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
                
            total = l1.val + l2.val + carry
            carry, value = divmod(total, 10)
            node = ListNode(value)
            if previous_node:
                previous_node.next = node
            
            previous_node = node
            l1 = l1.next
            l2 = l2.next
            if not first_node:
                first_node = node
                
        if carry:
            node = ListNode(carry)
            previous_node.next = node
            
        return first_node