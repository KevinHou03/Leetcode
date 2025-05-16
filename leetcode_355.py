import heapq
from collections import defaultdict, deque

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque) # order by views, userID -> (id, tweets)
        self.following = defaultdict(set) # userID ->set(followerID)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.following[userId]:
            self.following[userId].add(userId)
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []
        for followee in self.following[userId] | {userId}:
            for tweet in list(self.tweets[followee])[:10]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        return [tweetId for _, tweetId in sorted(heap, reverse=True)]


    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)