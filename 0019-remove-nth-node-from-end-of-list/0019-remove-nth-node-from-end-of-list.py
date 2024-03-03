# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # get a pointer after nth
        # get a pointer before nth
        
        # get size of list
        curr = head
        sz = 0
        while curr:
            curr=curr.next
            sz+=1
        
        dummy = ListNode()
        p1 = head
        p2 = dummy
        for _ in range(sz - n):
            
            p2.next = p1
            p2 = p2.next
            p1 = p1.next
            
        p2.next = p1.next if p1 and p1.next else None
        
        return dummy.next
            
            
        
        
        