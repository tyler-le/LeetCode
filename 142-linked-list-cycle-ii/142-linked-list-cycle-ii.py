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
        
        slow = fast = head
        
        # Look for cycle
        while fast is not None:
            if fast.next is None or fast.next.next is None:
                return None
            
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                break
                
        # cycle is found, look for head of cycle.
        # keep incrementing curr and fast and when they equal, that is the head of the cycle
        curr = head
        while curr is not fast:
            curr = curr.next
            fast = fast.next
            
        return fast
            
            