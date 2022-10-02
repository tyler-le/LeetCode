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
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        left = head
        right = prev
        
        l_next, r_next = head.next, prev.next
        while (left != r_next) and (right != l_next):            
            left.next = right
            right.next = l_next
            left = l_next
            right = r_next
            if left == right: break
            l_next = left.next
            r_next = right.next
            