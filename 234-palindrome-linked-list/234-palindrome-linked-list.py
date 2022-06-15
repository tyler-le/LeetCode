# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        # Look for middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse second half
        prev = None
        while slow != None:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Compare the two lists
        left, right = head, prev
        while left != None and right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
        