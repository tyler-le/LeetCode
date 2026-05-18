# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        def dfs(low, high):
            if low > high: return None
            mid = low + ((high - low) // 2)
            root_val = arr[mid]

            root = TreeNode(arr[mid])
            root.left = dfs(low, mid - 1)
            root.right = dfs(mid + 1, high)

            return root
        
        return dfs(0, len(arr) - 1)