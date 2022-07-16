# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        slow = fast = head
        
        # get middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse linked list from fast to end
        prev, curr, next_node = None, slow, None
        while curr:
            next_node = curr.next
            curr.next = prev
            
            prev = curr
            curr = next_node
            
        # inter-leave pointers
        l,r = head, prev
        while l and r:
            temp_l = l.next
            l.next = r
            l = temp_l
            temp_r = r.next
            r.next = l
            r = temp_r
            
        if not l and r:
            r.next = l
        if l and not r:
            l.next = r
            
        
            
        