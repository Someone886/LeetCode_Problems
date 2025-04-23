class Twitter:

    def __init__(self):
        self.user_tweets = {}
        self.user_following = {}
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append([self.order, tweetId])
        self.order += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        sourses = None
        if userId not in self.user_following:
            sourses = [userId]
        else:
            sourses = self.user_following[userId]
        
        heap = []
        cnt = 0

        for sourseId in sourses:
            if sourseId in self.user_tweets:
                for tweet in self.user_tweets[sourseId]:
                    heapq.heappush(heap, tweet)
                    cnt += 1
                    
                    if cnt > 10:
                        heapq.heappop(heap)
                        cnt -= 1
        
        ans = []
        for i in range(cnt):
            ans.append(heapq.heappop(heap)[1])
        
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_following:
            self.user_following[followerId] = set()
            self.user_following[followerId].add(followerId)

        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId in self.user_following.keys():
                self.user_following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)