# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        p1, p2 = list1, list2
        
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
                curr = curr.next
        
        if not p1:
            curr.next = p2
        
        elif not p2:
            curr.next = p1
                
        
        return dummy.next