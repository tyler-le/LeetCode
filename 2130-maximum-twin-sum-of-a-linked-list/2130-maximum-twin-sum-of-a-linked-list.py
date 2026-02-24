# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse_ll(p1):
            prev = None
            while p1:
                
                nxt = p1.next
                p1.next = prev
                prev = p1
                p1 = nxt
            
            return prev

        slow, fast = head, head
        slow_prev = None

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        slow_prev.next = None
        p1 = head
        p2 = reverse_ll(slow)
        res = 0

        while p1 != p2:
            res = max(res, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        
        return res
        
        