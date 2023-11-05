class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        num_wins = collections.defaultdict(int)
        
        while True:

            first, second = arr[0], arr[1]
            
            if first > second:
                # move second to end
                arr.remove(second)
                arr.append(second)
                num_wins[first]+=1
                
            else:
                # move first to end and second to first
                arr.remove(first)
                arr.append(first)
                arr[0] = second
                num_wins[second]+=1
                
            if num_wins[arr[0]] == k or num_wins[arr[0]] == len(arr): 
                return arr[0]
            
            

            
            