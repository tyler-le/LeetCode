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
        
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # disconnect left list from right list
        curr = slow.next
        prev = slow.next = None
        
        # reverse the right side
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # reconnect 
        left = head
        right = prev
        while right:
            l_next = left.next
            r_next = right.next
            left.next = right
            right.next = l_next
            left, right = l_next, r_next
            
                        