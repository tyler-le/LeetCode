# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        currA = headA
        currB = headB

        while currA:
            visited.add(currA)
            currA = currA.next
        
        while currB:
            if currB in visited: return currB
            currB = currB.next
        
        return None