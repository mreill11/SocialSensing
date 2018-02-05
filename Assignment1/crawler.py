#boring auth you already have
import tweepy
from tweepy import OAuthHandler
CONSUMER_KEY = 'cue6yOS0gH1lQ9XYRfSvt7zPD'
CONSUMER_SECRET = 'OTSlghuTGdDwMlG4N7twuEPtZDBdjqpAlEZtQDARTYGvVs1YEh'
ACCESS_KEY = '793906953755951105-gvQ7tqhU7g2wwfcw1yw96zGGGcjiHfa'
ACCESS_SECRET = '8pGfOsYfgd3mVY3SVi8tAWukPLg7htePEFOgyaCmIQBXS'
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#search
api = tweepy.API(auth)
test = api.lookup_users(user_ids=['34373370, 26257166, 12579252'])

# f = open('user_info.txt', 'w')
#
# for user in test:
#     f.write("Screen Name: " + user.screen_name + "\n")
#     f.write("User Name: " + user.name + "\n")
#     f.write("User Description: " + user.description + "\n")
#     f.write("Number of Followers: %d\n" % user.followers_count)
#     f.write("Number of Friends: %d\n" % user.friends_count)
#     f.write("Number of Statuses: %d\n" % user.statuses_count)
#     f.write("User's URL: " + user.url + "\n")
#     f.write("\n")
#
# f.close()
#
# f = open('user_network.txt', 'w')
# for user in test:
#     user_followers = tweepy.Cursor(api.followers, screen_name=user.screen_name).items(20)
#     f.write("\nThe Followers List:\n\n")
#     for u in user_followers:
#         f.write(u.screen_name + "\n")
#     user_friends = tweepy.Cursor(api.friends, screen_name=user.screen_name).items(20)
#     f.write("\nThe Friends List:\n\n")
#     for u in user_friends:
#         f.write(u.screen_name + "\n")
#
# f.close()

f = open('keyword_tweets.txt', 'w')
query = '"Indiana" OR "weather"'
maxTweets = 50
for tweet in tweepy.Cursor(api.search,q=query).items(maxTweets):
    f.write(tweet.text.encode('utf-8') + "\n")
f.close()

f = open('location_tweets.txt', 'w')
numTweets = 0
class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global numTweets
        if numTweets <= 50:
            f.write(status.text.encode('utf-8') + "\n")
            numTweets += 1
        else:
            return True

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[-86.33,41.63,-86.20,41.74])
