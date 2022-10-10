class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        triplets = [(u, t, w) for u, t, w in zip(username, timestamp, website)]
        triplets.sort(key = lambda i : (i[1]))

        hmap = collections.defaultdict(list)
        patterns = collections.defaultdict(int)
        
        for user, time, website in triplets:
            hmap[user].append(website)
        
        for user, history in hmap.items():
            for pattern in (set(combinations(history, 3))):
                patterns[pattern]+=1
        print(patterns)
        return max(sorted(patterns), key=patterns.get)