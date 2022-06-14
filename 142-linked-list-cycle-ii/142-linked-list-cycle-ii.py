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
        
        while fast is not None:
            if fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
                
        curr = head
        while curr is not fast:
            curr = curr.next
            fast = fast.next
            
        return fast
            
            