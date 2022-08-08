# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        curr = head
        prev = dummy
        # get to position
        for _ in range(left-1):
            prev = curr
            curr = curr.next
            
        head = prev    
        # perform reversal for right-left+1 iters
        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        head.next.next = curr
        head.next = prev
        
    
        return dummy.next
            