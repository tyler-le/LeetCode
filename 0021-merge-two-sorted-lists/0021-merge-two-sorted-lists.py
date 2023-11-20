# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        head = ListNode()
        p1, p2, curr = list1, list2, head

        while p1 and p2:
            
            if p1.val < p2.val: 
                curr.next = ListNode(p1.val)
                p1 = p1.next
                
            else: 
                curr.next = ListNode(p2.val)
                p2 = p2.next

            curr = curr.next
            
        if p1 and not p2: curr.next = p1
        else: curr.next = p2
            
        return head.next
                    
                
                