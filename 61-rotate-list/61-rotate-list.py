# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        tail, list_len = head, 1

        while tail.next is not None:
            tail = tail.next
            list_len+=1
        
        k = k % list_len
        if k == 0:
            return head
        
        curr = head
        for i in range(list_len - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        tail.next = head
        
        return new_head
            
        
       
            
            
        