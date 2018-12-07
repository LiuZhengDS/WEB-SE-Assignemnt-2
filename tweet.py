from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="PVYZeIanYS9ft2btJUDqYcTKu"
consumer_secret="aszsvt7jOz0k6bvhlVPURPJlgtAhQc4EqnjfWgL6e9oxWqQ04P"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1070282938183507968-4lei75Kt0GnxZ8v6I3wFeE5XjdP0iw"
access_token_secret="gwebqVXS7byweIsG4pNdManODoauhzd0KhdUrvK9YnzRc"

#
TimePeriod_Second = 60 * 60 * 2


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self):
        self.starttime = time.time()
        self.tweets_counter = 0
        self.en_counter = 0
        self.nl_counter = 0

    def on_data(self, jsondata):
        print(jsondata)
        data = json.loads(jsondata)
        if data.has_key('lang') == True:
            language = data['lang']
            self.tweets_counter = self.tweets_counter + 1
            if language == "en":
                self.en_counter = self.en_counter + 1
            elif language == "nl":
                self.nl_counter = self.nl_counter + 1
        # elif language == "":
        #     nl_counter = nl_counter + 1
        # with open('data.json', 'a') as file:
        #     file.write(data)

        if time.time() <= self.starttime + TimePeriod_Second:
            return True
        else:
            return False

    def on_error(self, status):
        print(status)

# API.home_timeline(17:21, 17:31)
# API.reverse_geocode([lat][, long][, accuracy][, granularity][, max_results])

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    # Location of Schipol
    # stream.filter(locations = [4.73, 52.29, 4.77, 52.32])

    # Location of Amsterdam
    #stream.filter(locations = [4.112784, 51.761243, 5.468162, 52.52808])

    # coordinates":[[[4.112784,51.761243],[4.112784,52.52808],[5.468162,52.52808],[5.468162,51.761243],[4.112784,51.761243]

    # stream.filter(track=['basketball'])

    # stream.filter(locations = 'Amsterdam')
    # Location of Schipol
    stream.filter(locations = [4.73,52.29,4.98,52.42])
    # print "The number of English tweets is:"
    print(l.en_counter)
    # print "\n"

    # print "The number of Dutch tweets is:"
    print(l.nl_counter)
    # print "\n"

    # print "The number of tweets from Amsterdam is:"
    print(l.tweets_counter)
    # print "\n"

    # print "The number of tweets from Amsterdam is:"
    print()
    # print "\n"
