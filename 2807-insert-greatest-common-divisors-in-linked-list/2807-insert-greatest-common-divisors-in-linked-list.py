# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        first, second = head, head.next
        
        while second:
            gcd = math.gcd(first.val, second.val)
            node = ListNode(gcd, None)
            
            first.next = node
            node.next = second
            
            first = second
            second = second.next
            
        return head
