import json

from TwitterAPI import TwitterAPI

from keys import consumer_key, consumer_secret, access_key, access_secret

def get_tweet_count(user):
    arguments = { 'screen_name': user, 'count': 1 }
    r = api.request('statuses/user_timeline', arguments)
    tweet = r.json()[0]
    return tweet['user']['statuses_count'], tweet['id']

def get_200_tweets(user, max_id):
    arguments = { 'screen_name': user, 'count': 200, 'max_id': max_id }
    r = api.request('statuses/user_timeline', arguments)
    tweets = r.json()
    return tweets

def main():
    tweet_count, max_id = get_tweet_count('jamessamsf')

    # TODO: FIGURE OUT HOW TO ITERATE OVER THE TIMELINE IN CHUNKS. DO I NEED TO
    # FIND THE FIRST AND LAST TWEET IDs?

if __name__ == '__main__':
    api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)
    main()
