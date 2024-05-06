# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # monotonic increasing stack
        # build LL from stack
        
        stack = []
        curr = head
        
        while curr:
                
            while stack and curr.val > stack[-1]:
                stack.pop()
                
            stack.append(curr.val)
            curr = curr.next
            
        dummy = ListNode()
        curr = dummy
        for x in stack:
            curr.next = ListNode(x)
            curr = curr.next
            
        return dummy.next
            