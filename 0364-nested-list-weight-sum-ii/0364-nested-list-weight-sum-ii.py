# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        # find max_depth
        def max_depth(arr):
            res = 0
            print(arr)
            for elem in arr:
                if elem.isInteger(): res = max(res, 1)
                else: res = max(res, 1 + max_depth(elem.getList()))
            return res

        mx_depth = max_depth(nestedList)

    
        # calculate sums
        def calculate_sums(arr, curr_depth):
            nonlocal mx_depth
            res = 0
            for elem in arr:
                if elem.isInteger(): res += elem.getInteger() * (mx_depth - curr_depth + 1)
                else: res+=(calculate_sums(elem.getList(), curr_depth + 1))
            return res
            
        
        return calculate_sums(nestedList, 1)
        