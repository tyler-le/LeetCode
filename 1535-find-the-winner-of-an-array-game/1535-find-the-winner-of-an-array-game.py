class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        winstreak = 0
        maxi = max(arr)
        
        while True:

            first, second = arr[0], arr[1]
            if first == maxi: return maxi
            
            if first > second:
                # move second to end
                arr.remove(second)
                arr.append(second)
                winstreak+=1
                
            else:
                # move first to end and second to first
                arr.remove(first)
                arr.append(first)
                arr[0] = second
                winstreak = 1
                
            if winstreak == k:
                return arr[0]
            
            # early exit
            if winstreak == len(arr): 
                return arr[0]
            
            

            
            