class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        winstreak = 0
        maxi = max(arr)
        q = deque(arr[1:])
        curr = arr[0]
        
        while q:

            opponent = q.popleft()
            if curr == maxi: return maxi
            
            if curr > opponent:
                # move second to end
                q.append(opponent)
                winstreak+=1
                
            else:
                # move first to end and second to first
                q.append(curr)
                curr = opponent
                winstreak = 1
                
            if winstreak == k:
                return curr
            
            # early exit
            if winstreak == len(arr): 
                return curr
            
            

            
            