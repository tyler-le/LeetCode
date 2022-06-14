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
        
        my_set = set()
        curr = head
        
        while (curr is not None):
            if curr in my_set:
                return curr
            
            my_set.add(curr)
            curr = curr.next
        
        return None
        