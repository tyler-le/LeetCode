class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hmap = collections.defaultdict(list)
        patterns = collections.defaultdict(int)
        
        for user, site, time in sorted(zip(username, website, timestamp), key = lambda i : (i[0], i[2])):
            hmap[user].append(site)
            
        patterns = Counter()

        for user, sites in hmap.items():
            patterns.update(Counter(set(combinations(sites, 3))))

        return max(sorted(patterns), key=patterns.get)