# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            if not node: return None
        
            prev = None
            curr = node
            nxt = curr.next

            while curr:
                nxt = curr.next;
                curr.next = prev
                prev = curr
                curr = nxt

            return prev
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = reverse(slow)
        
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        
        return True