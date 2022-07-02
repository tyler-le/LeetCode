# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_a, curr_b = headA, headB
        
        while True:
            if curr_a is None and curr_b is None:
                return None
            
            elif curr_a is curr_b:
                return curr_a
            
            
            curr_a = headB if (curr_a is None) else curr_a.next
            curr_b = headA if (curr_b is None) else curr_b.next