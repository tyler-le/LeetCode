# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        curr = head
        counter = 0
        while curr:
            curr = curr.next
            counter+=1
            
        if n == counter:
            head = head.next
            return head
            
        for _ in range(n): fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head