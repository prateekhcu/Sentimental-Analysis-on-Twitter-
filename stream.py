#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3279582007-sdKKHwE1tNhA2ZnDFa9w1U4U3r0anJjxOxAqGKF"
access_token_secret = "LUcpzqb2mK7O1bIt16QLzLVfFiXAaVJp7dzbw7Umy9EcQ"
consumer_key = "KP8OmHv6ravfQKoxqjfo8U0bO"
consumer_secret = "scCnpdpH7OM0g3SQ037it0qgyAFc4kt0f0VZYZJ0JKXn9bwx7z"

#f1=open("tweet01jul.txt",'w')
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        #f2.write("%s\n"%(data))
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'

setTerms = ['bajrangi bhaijaan']
stream.filter(track = setTerms)

    #stream.filter(track=[''])

