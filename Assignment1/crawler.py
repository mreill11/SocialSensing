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

for user in test:
    print "Screen Name: " + user.screen_name
    print "User Name: " + user.name
    print "User Description: " + user.description
    print "Number of Followers: %d" % user.followers_count
    print "Number of Statuses: %d" % user.statuses_count
    print "User's URL: " + user.url
    print "\n"
