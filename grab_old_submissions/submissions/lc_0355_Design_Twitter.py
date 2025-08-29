#MAJOR MISTAKE: Didn't handle re-following the same person.

from collections import defaultdict
from heapq import heappush,heappop

class Twitter:

    def __init__(self):
        '''
        Need:
         - sequence #
         - map from user to tweet heap
         - map from user to self-tweet stack
         - map from user to follower set
        '''
        self.seq_num = 0
        self.user_to_feed_heap = defaultdict(list)
        self.user_to_authored_tweets = defaultdict(list)
        self.user_to_followers = defaultdict(set)
        self.user_to_following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # user's tweet is pushed to all follower's tweetheaps (and our own)
        # We'll do this by checking all followers of this user and pushing to each heap.
        # We should push the sequence number, the user id, and the tweet id
        # TC: O(n_followers*log(k)) where k is the total number of tweets in the universe
        follower_ids = self.user_to_followers[userId]
        heappush(self.user_to_feed_heap[userId],(-self.seq_num,userId,tweetId))
        for follower_ids in follower_ids:
            heappush(self.user_to_feed_heap[follower_ids],(-self.seq_num,userId,tweetId)) # TODO: just pass tweetId, then in getNewsFeed, lookup the userID. More space-efficient
        self.user_to_authored_tweets[userId].append((-self.seq_num,tweetId))
        self.seq_num+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # We'll assemble the list by popping from the heap and comparing against
        # the hashset of followees, until we have 10; then we'll push elements back into the heap.
        # TC: log(k) where k is the total number of tweets in the universe, on average
        result = []
        seq_nums_seen = set()
        feed_heap = self.user_to_feed_heap[userId]
        following = self.user_to_following[userId]
        while len(seq_nums_seen) < 10 and feed_heap:
            tweet_data = heappop(feed_heap)
            if (tweet_data[1] not in following and tweet_data[1] != userId) or tweet_data[0] in seq_nums_seen:
                continue
            result.append(tweet_data)
            seq_nums_seen.add(tweet_data[0])
        for tweet_data in result:
            heappush(feed_heap,tweet_data)
        return [elem[2] for elem in result]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Here we (1) add to followee's set of followers;
        # (2) Update follower's tweetheap with top 10 followee's tweets
        # (3) add to followers set of following
        if followerId in self.user_to_followers[followeeId] or followerId == followeeId:
            return
        self.user_to_followers[followeeId].add(followerId) # 1
        self.user_to_following[followerId].add(followeeId) # 3
        tweets_to_add = self.user_to_authored_tweets[followeeId]
        if len(tweets_to_add) == 0:
            return
        starting_index = -10 if len(tweets_to_add)>10 else 0
        copied_tweets = tweets_to_add[starting_index:]
        for tweet in copied_tweets:
            heappush(self.user_to_feed_heap[followerId],(tweet[0],followeeId,tweet[1]))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Here we (1) remove from followee's set of followers
        # and (2) remove from follower's set of following
        # We let tweetheap update on read.
        # TC: O(1)
        self.user_to_followers[followeeId].discard(followerId)
        self.user_to_following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)