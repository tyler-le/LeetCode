# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        curr = head
        arr = []
        res = 0
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        left, right = 0, len(arr) - 1
        
        while left < right:
            res = max(res, arr[left] + arr[right])
            left+=1
            right-=1
        
        return res
            
        