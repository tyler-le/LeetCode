# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None
        
        def merge(list1, list2):
            dummy = ListNode()
            l1, l2, curr = list1, list2, dummy

            while l1 and l2:
                if l1.val < l2.val: 
                    curr.next = l1
                    l1 = l1.next
                else: 
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1 and not l2: curr.next = l1
            elif not l1 and l2: curr.next = l2

            return dummy.next

        while len(lists) > 1:
            first, second = lists.pop(), lists.pop()
            lists.append(merge(first, second))
            
        return lists[0]
            
            
        
        