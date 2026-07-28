from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, userId, self.time, len(self.posts[userId])))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.follows[userId].add(userId)
        heap = []

        for followee in self.follows[userId]:
            if self.posts[followee]:
                tweet, user, time, idx = self.posts[followee][-1]
                heap.append((-time, user, tweet, idx))
        
        heapq.heapify(heap)

        while heap and len(feed) < 10:
            time, user, tweet, idx = heapq.heappop(heap) 
            feed.append(tweet)
            if idx > 0:
                tweet, poster, time, idx1 = self.posts[user][idx-1]
                heapq.heappush(heap, (-time, poster, tweet, idx1))
        return feed            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
