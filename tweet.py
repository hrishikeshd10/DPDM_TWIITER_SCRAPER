class Tweet:

    def __init__(self, tweetText, views, reposts, quotes, likes, bookmarks, timeStamp,userHandle):
        self.tweetText = tweetText
        self.views = views
        self.reposts = reposts
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
        return self.reposts

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

