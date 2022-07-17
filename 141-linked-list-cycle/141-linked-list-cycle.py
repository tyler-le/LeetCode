# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        if not slow:
            return False 
        
        while True:
            if slow.next:
                slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
            
            if fast == slow:
                return True
            