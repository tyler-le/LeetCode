class Twitter:

    def __init__(self):
        # map user to all their tweets
        self.tweet_map = defaultdict(deque)
        
        # map user id -> people they follow
        self.follower_map = defaultdict(set)
        
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.tweet_map[userId].append((self.timestamp, tweetId))
        self.timestamp+=1
        
            

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        for follower in self.follower_map[userId]:
            all_tweets+=list(self.tweet_map[follower])
        
        all_tweets.sort(key = lambda x : x[0], reverse=True)
        
        if len(all_tweets) < 10: return [tweet for _, tweet in all_tweets]
        return [tweet for _, tweet in all_tweets[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followerId)
        self.follower_map[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_map[followerId]:
            self.follower_map[followerId].remove(followeeId)
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)