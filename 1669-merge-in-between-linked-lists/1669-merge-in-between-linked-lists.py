# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        before_a = None
        current_b = None
        curr = list1
        back_list2 = list2
        
        
        
        for i in range(b+1):
            if i == a-1: before_a = curr
            if i == b: current_b = curr
            curr = curr.next
        
        while back_list2 and back_list2.next:
            back_list2 = back_list2.next
            
        before_a.next = list2
        back_list2.next = current_b.next
        return list1