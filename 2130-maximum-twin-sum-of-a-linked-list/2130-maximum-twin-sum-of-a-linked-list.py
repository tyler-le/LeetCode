# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        res = 0
        l, r = 0, len(arr) - 1

        while l < r:
            res = max(res, arr[r] + arr[l])
            l+=1
            r-=1
        
        return res
