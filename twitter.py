import json
import os

from TwitterAPI import TwitterAPI

from keys import consumer_key, consumer_secret, access_key, access_secret

high = []; mid = []; low = []

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

def parse_tweets(tweets, max_id):
    for tweet in tweets:
        if tweet['id'] == max_id:
            continue
        if 'RT @' in tweet['text']:
            continue
        if tweet['retweet_count'] == 0:
            continue
        if tweet['retweet_count'] >= 10:
            high.append(tweet)
            continue
        if tweet['retweet_count'] >= 5:
            mid.append(tweet)
            continue
        if tweet['retweet_count'] >= 1:
            low.append(tweet)            

def main():
    user = 'jamessamsf'
    tweet_count, max_id = get_tweet_count(user)

    while tweet_count > 0:
        tweets = get_200_tweets(user, max_id)
        parse_tweets(tweets, max_id)
        max_id = tweets[-1]['id']
        tweet_count -= 200

    # Write the results
    print('low: {}, mid: {}, high: {}'.format(len(low), len(mid), len(high)))

    if not os.path.exists('results'):
        os.mkdir('results')
    with open('results/low.json', 'w') as low_file:
        low_file.write(json.dumps(low, sort_keys=True, indent=4))
    with open('results/mid.json', 'w') as mid_file:
        mid_file.write(json.dumps(mid, sort_keys=True, indent=4))
    with open('results/high.json', 'w') as high_file:
        high_file.write(json.dumps(high, sort_keys=True, indent=4))

if __name__ == '__main__':
    api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)
    main()
