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
        
        # first find max_depth. needed to calc weight
        def max_depth_finder(nestedList, curr_depth):
            max_depth = curr_depth
        
            for nested in nestedList:
                if nested.getList():
                    max_depth = max(max_depth, max_depth_finder(nested.getList(), curr_depth + 1))

            return max_depth
            
            
        def dfs(nestedList, depth, max_depth):
            res = 0
            for nested in nestedList:
                if nested.isInteger():
                    weight = max_depth - depth + 1
                    res+=(nested.getInteger() * weight)
                else:
                    res+=dfs(nested.getList(), depth+1, max_depth)
     
            return res
            
        max_depth = max_depth_finder(nestedList, 1)
        return dfs(nestedList, 1, max_depth)
        
        