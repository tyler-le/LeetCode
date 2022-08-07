# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        
        # store (key, Node) pairs in array, sort, reconnect
        container = []
        
        curr = head
        while curr:
            container.append([curr.val, curr])
            curr = curr.next
            
        container.sort(key = lambda i : i[0])
        
        prev, head = None, container[0][1]
        for val, node in container:
            if prev: prev.next = node
            prev = node
            
        prev.next = None
        return head
                
            
            