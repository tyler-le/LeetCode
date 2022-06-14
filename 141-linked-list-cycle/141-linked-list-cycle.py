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
        
        while fast != None:
            if fast.next == None or fast.next.next == None:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
            
        return False
            
        