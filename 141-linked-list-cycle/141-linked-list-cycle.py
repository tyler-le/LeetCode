# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        while fast is not None:
            if fast.next is None or fast.next.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if fast is slow:
                return True
            
        return False
            
        