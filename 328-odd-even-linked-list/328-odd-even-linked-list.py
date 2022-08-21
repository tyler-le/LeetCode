# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        
        odd_head, even_head = head, head.next
        
        
        odd_slow = odd_fast = odd_head
        even_slow = even_fast = even_head
        
        while even_fast and even_fast.next:
            odd_fast = odd_fast.next.next
            odd_slow.next = odd_fast
            odd_slow = odd_fast
            
            even_fast = even_fast.next.next
            even_slow.next = even_fast
            even_slow = even_fast
        odd_slow.next = even_head
        return odd_head
            
        