# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = {}
        dummy = ListNode()
        dummy.next = head
        
        curr = head
        while curr:
            count[curr.val] = 1 + count.get(curr.val, 0)
            curr = curr.next
            
            
        curr = dummy
        while curr and curr.next:
            if count[curr.next.val] >= 2:
                count[curr.next.val]-=1
                curr.next = curr.next.next
            else:
                curr = curr.next
                
            
        return dummy.next
        