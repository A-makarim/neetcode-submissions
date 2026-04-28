class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) # whos who did what tweet
        self.time = 0
        self.follows = defaultdict(list) # knows who follows who
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -=1
        self.tweets[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetsbyallusers = []
        ans = []


        for i in self.follows[userId]:
            tweetsbyallusers.append(self.tweets[i])

        heapq.heapify(tweetsbyallusers)
        heapq.heappush(tweetsbyallusers, self.tweets[userId])
        for i in range(10):
            if not tweetsbyallusers: 
                return ans
            poopin = heapq.heappop(tweetsbyallusers)
            ans.append(poopin[0][1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:   # user 1 follows user 2. user 2 follower in user 1 
        self.follows[followerId].append(followeeId)
        # user1 is the key. followers are the values
        print(self.follows)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].remove(followeeId)

        
