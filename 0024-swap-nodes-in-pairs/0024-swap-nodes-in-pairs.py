# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(node):
            if not node: return None
            if not node.next: return node
            
            first, second, third = node, node.next, node.next.next
            second.next = first
            first.next = helper(third)
            return second
            
            
        
        return helper(head)
            