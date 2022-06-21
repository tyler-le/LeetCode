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
        
        counter = head
        list_len = 0
        
        while counter is not None:
            list_len+=1
            counter = counter.next
        
        if list_len == 0:
            return None
        
        new_head_index = (list_len - k) % list_len
        
        new_head = head
        for i in range(new_head_index):
            new_head = new_head.next

        curr = new_head
        for j in range(list_len - 1):
            if curr.next is None:
                curr.next = head
            curr = curr.next
            
        curr.next = None
        
        return new_head
            
        
       
            
            
        