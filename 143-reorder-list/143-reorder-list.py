# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find middle of list
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half
        prev = None
        while slow != None:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # reconnect zigzag list
        l,r,l_next,r_next = head, prev, head.next, prev.next
       
        while l != r_next and r != l_next:
            l.next = r
            r.next = l_next
            l = l_next
            r = r_next
            if l==r:
                break
                
            l_next = l.next
            r_next = r.next
        