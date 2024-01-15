# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
            
        prev = None
        curr = head
        nxt = curr.next
        
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if curr: nxt = curr.next
        
        return prev