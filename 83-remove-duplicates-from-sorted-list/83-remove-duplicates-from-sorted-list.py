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
        
        curr = dummy
        while curr and curr.next:
            count[curr.next.val] = 1 + count.get(curr.next.val, 0)
            if count[curr.next.val] >= 2:
                count[curr.next.val]-=1
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return dummy.next
        