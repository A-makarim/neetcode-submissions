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
        for i in self.follows[userId]:  # user 2 has 1
            if self.tweets[i]:  # tweets by 1
                tweetsbyallusers.extend(self.tweets[i])

        if self.tweets[userId]:
            tweetsbyallusers.extend(self.tweets[userId])
        heapq.heapify(tweetsbyallusers)
        
            
        print(tweetsbyallusers)
        for i in range(10):
            if not tweetsbyallusers:
                print("breaking") 
                return ans
            poopin = heapq.heappop(tweetsbyallusers)
            print(poopin)
            ans.append(poopin[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:   # user 1 follows user 2. user 2 follower in user 1 
        if followerId != followeeId:
            self.follows[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].remove(followeeId)

        
