class Solution:
    def jump(self, nums: List[int]) -> int:
        
        q = deque([(0,0)])
        n = len(nums)
        visited = set()
        
        while q:
            idx, steps = q.popleft()
    
            if idx == n-1: return steps
            for x in range(1, nums[idx]+1):
                if (idx+x) < n and (idx+x) not in visited: 
                    q.append((idx+x, steps+1))
                    visited.add(idx+x)
            
