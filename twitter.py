import json

from TwitterAPI import TwitterAPI

from keys import consumer_key, consumer_secret, access_key, access_secret

def get_tweet_count(user):
    r = api.request('statuses/user_timeline',
        { 'screen_name': user, 'count': 1 })
    tweet = r.json()[0]
    # with open('test.txt', 'w') as test:
    #     test.write(json.dumps(tweet, indent=4, sort_keys=True))
    return tweet['user']['statuses_count']

def main():
    tweet_count = get_tweet_count('jamessamsf')
    print(tweet_count)

if __name__ == '__main__':
    api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)
    main()
