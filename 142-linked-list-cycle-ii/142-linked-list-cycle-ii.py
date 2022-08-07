# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        print(fast)
        if not fast or not fast.next: 
            return None
        
        slow2 = head
        while fast is not slow2:
            fast = fast.next
            slow2 = slow2.next
            
        return slow2
            