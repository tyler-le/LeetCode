# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []
        acc = 0
        curr = head.next
        dummy = ListNode()
        ptr = dummy
        
        while curr:
            if curr.val == 0: 
                ptr.next = ListNode(acc)
                ptr = ptr.next
                acc = 0
            else: 
                acc+=curr.val
            
            curr = curr.next
        return dummy.next