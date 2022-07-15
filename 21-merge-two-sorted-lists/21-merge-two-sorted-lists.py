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
        
        first, second = list1, list2
        head = ListNode(-1)
        curr = head
        
        while first and second:
            if first.val < second.val:
                curr.next = ListNode(first.val)
                curr = curr.next
                first = first.next
            else:
                curr.next = ListNode(second.val)
                curr = curr.next
                second = second.next
                
        if first and not second:
            curr.next = first
        elif second and not first:
            curr.next = second
                
        return head.next