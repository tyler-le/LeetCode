class Solution:
    def numTrees(self, n: int) -> int:
        cache = defaultdict(int)
        cache[0] = 1
        cache[1] = 1
        
        for num_nodes in range(2, n+1):
            for middle in range(1, num_nodes + 1):
                left_num_nodes = middle - 1
                right_num_nodes = num_nodes - middle
                cache[num_nodes] = cache[num_nodes] + (cache[left_num_nodes] * cache[right_num_nodes])
        
        return cache[n]
                
    