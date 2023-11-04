class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        postfix = []
        maxi = arr[-1]
        
        for i in range(len(arr)-1, 0, -1):
            maxi = max(arr[i], maxi)
            postfix.append(maxi)
            
        postfix.reverse()
        postfix.append(-1)
        
        return(postfix)