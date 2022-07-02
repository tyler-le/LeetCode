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
            
            if curr_a is None:
                curr_a = headB
            else:
                curr_a = curr_a.next    
                
            if curr_b is None:
                curr_b = headA
            else:
                curr_b = curr_b.next