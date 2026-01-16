# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, sum2 = 0, 0

        def find_sum(node):
            summ, power = 0, 0
            while node:
                summ+=(node.val * 10**power)
                power+=1
                node = node.next
            return summ

        total = find_sum(l1) + find_sum(l2)
        dummy = ListNode(0)
        if not total: return dummy

        curr = dummy
        while total:
            curr.next = ListNode(total % 10)
            curr = curr.next
            total = total // 10

        return dummy.next

