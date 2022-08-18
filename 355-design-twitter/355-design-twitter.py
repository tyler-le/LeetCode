class Tweet:
    def __init__(self, user_id, tweet_id):
        self.user_id = user_id
        self.tweet_id = tweet_id

class User:
    def __init__(self):
        self.following = set()
        

class Twitter:

    def __init__(self):
        self.user_map = defaultdict(User)
        self.all_tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweet(userId, tweetId)
        self.all_tweets.append(tweet)
            

    def getNewsFeed(self, userId: int) -> List[int]:
        count, res = 0, []
        for i in range(len(self.all_tweets)-1, -1, -1):
            if count == 10: break
            if self.all_tweets[i].user_id in self.user_map[userId].following \
                or self.all_tweets[i].user_id == userId:
                res.append(self.all_tweets[i].tweet_id)
                count+=1
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map[followerId].following:
            self.user_map[followerId].following.add(followerId)
        self.user_map[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_map: 
            self.user_map[followerId].following.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)