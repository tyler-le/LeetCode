# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = head, head.next

        while curr:

            # cur is out of order, insert it to front position
            if curr.val < prev.val:
                tmp = dummy
                
                # find insertion point
                while tmp.next.val < curr.val:
                    tmp = tmp.next
                
                # insert
                prev.next = curr.next
                curr.next = tmp.next
                tmp.next = curr
                curr = prev.next
            
            else:
                prev, curr = curr, curr.next
        
        return dummy.next
                