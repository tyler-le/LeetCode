# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        power, curr, l1_val = 0, l1, 0
        while curr:
            l1_val+=curr.val * (10**power)
            curr = curr.next
            power+=1
        
        power, curr, l2_val = 0, l2, 0
        while curr:
            l2_val+=curr.val * (10**power)
            curr = curr.next
            power+=1
            
        head = ListNode() 
        curr = head
        sumi = reversed(str(l1_val + l2_val))
        for ch in sumi:
            curr.next = ListNode(int(ch))
            curr = curr.next
            
        return head.next
            
        
        