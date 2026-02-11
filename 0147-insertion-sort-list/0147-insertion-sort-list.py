# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # INVARIANTS:
        # 1. prev is the last node in the sorted portion
        # 2. curr is the current node we are sorting
        # 3. temp is the insertion point of where we want curr to end up

        prev, curr = head, head.next

        while curr:

            # if sorted, continue
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next

            # else it's 'curr' is at an unsorted position
            else:
                # find the insertion point using `tmp`
                tmp = dummy
                while curr.val > tmp.next.val:
                    tmp = tmp.next
                
                # insert curr at that insertion point
                prev.next = curr.next
                curr.next = tmp.next
                tmp.next = curr
                curr = prev.next
        
        return dummy.next
