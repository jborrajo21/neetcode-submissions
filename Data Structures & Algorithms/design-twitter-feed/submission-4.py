from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        maxHeap = []
        
        for followee in self.follows[userId]:
            posts = self.posts[followee]
            if posts:
                index = len(posts) - 1
                maxHeap.append((-posts[index][0], posts[index][1], followee, index - 1 if index - 1 >= 0 else None))
        heapq.heapify(maxHeap)
        feed = []

        while maxHeap and len(feed) < 10:
            post = heapq.heappop(maxHeap)
            feed.append(post[1])
            if post[3] != None:
                posts = self.posts[post[2]]
                idx = post[3]
                heapq.heappush(maxHeap, (-posts[idx][0], posts[idx][1], post[2], idx - 1 if idx - 1 >= 0 else None))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
