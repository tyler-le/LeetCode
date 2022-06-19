# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, prev = head,dummy
        
        for i in range(left-1):
            prev = curr
            curr = curr.next
        left_prev = prev
        prev = None
        for i in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        left_prev.next.next = curr
        left_prev.next = prev
        
        return dummy.next

        