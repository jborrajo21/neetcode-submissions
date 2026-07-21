from collections import defaultdict
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = []
        heapq.heapify(self.posts)
        self.ids = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.posts, (-self.ids, tweetId, userId))
        self.ids += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        counter = 0
        feed = []
        posts = self.posts.copy()
        heapq.heapify(posts)
        while posts and counter < 10:
            post = heapq.heappop(posts)
            if post[2] == userId or post[2] in self.follows[userId]:
                feed.append(post[1])
                counter += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
