class Tweet:

    def __init__(self, tweetText="NA", views="NA", retweets="NA", quotes="NA", likes="NA", bookmarks="NA", timeStamp="NA", userHandle="NA"):
        self.tweetText = tweetText
        self.views = views
        self.retweets = retweets
        self.quotes = quotes
        self.likes = likes
        self.bookmarks = bookmarks
        self.userHandle = userHandle
        self.timeStamp = timeStamp


    def getTweet(self):
        return self.tweetText

    def get_views(self):
        return self.views

    def get_reposts(self):
        return self.retweets

    def get_quotes(self):
        return self.quotes

    def get_likes(self):
        return self.likes

    def get_bookmarks(self):
        return self.bookmarks

    def get_userHandle(self):
        return self.userHandle

    def get_timeStamp(self):
        return self.timeStamp

    def get_tweet_as_list(self):
        return [self.userHandle, self.tweetText,  self.likes, self.timeStamp]

