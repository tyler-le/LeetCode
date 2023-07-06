# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1, p2 = list1, list2
        dummy = ListNode()
        curr = dummy
        
        
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
                
            curr = curr.next
            
        if not p1:
            curr.next = p2
        else:
            curr.next = p1
            
        return dummy.next
            
            