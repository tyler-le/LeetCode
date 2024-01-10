class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        hmap = defaultdict(int)
        cnt = 0
        res = []
        
        for a, b in zip(A, B):
            hmap[a]+=1
            hmap[b]+=1
            
            if a != b:
                if hmap[a] == 2: cnt+=1
                if hmap[b] == 2: cnt+=1
            else:
                if hmap[a] == 2: cnt+=1
            res.append(cnt)
        
        return res
            
            
            
            # 1 -> 2
            # 3 -> 2