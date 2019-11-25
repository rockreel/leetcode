class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        import heapq
        self.tweet_map = defaultdict(list)  # User id to its tweet.
        self.follow_map = defaultdict(set)  # User id to who it follows.
        self.seq_id = 0  # Seq id to sort tweet by time.
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweet_map[userId].append((self.seq_id, tweetId))
        self.seq_id += 1
    
    
    def _pushFeeds(self, feeds, tweet):
        if len(feeds) < 10:
            heapq.heappush(feeds, tweet)
        elif tweet[0] > feeds[0][0]:
            heapq.heappop(feeds)
            heapq.heappush(feeds, tweet)
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feeds = []
        # Get followee's tweets.
        for followee in self.follow_map[userId]:
            for tweet in self.tweet_map[followee]:
                self._pushFeeds(feeds, tweet)
        # Get user's own tweets.
        for tweet in self.tweet_map[userId]:
            self._pushFeeds(feeds, tweet)
        return [t[1] for t in sorted(feeds, reverse=True)]
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

