"""This is the daemon that stores tweets to REDIS"""
import redis
import redis.connection
import time

from datetime import timedelta
from itertools import chain
from newsfeed.tweets import get_tweets
from newsfeed.pre_processing import (remove_stopwords,
                                     lemmatize,
                                     is_viewable_tweet)

SEARCH_TERMS = ("(genenetwork OR "
                "genenetwork2 OR rat OR mouse OR pangenome OR "
                "browser OR workflows OR bioinformatic OR "
                "GeneNetwork OR conference OR sequences OR "
                "genotype OR phenotype OR guix OR RDF OR SPARQL "
                "OR genome OR biology OR Genomics OR OPAR OR genetics "
                "OR research OR ontologies OR variation)")
USERS = ("wolfgangkhuber,MarkGerstein,mstephens999")


if __name__ == "__main__":
    redis_conn = redis.Redis()
    while True:  # Daemon that keeps running forever:
        tweets = [get_tweets(user_name=user,
                             search_term=SEARCH_TERMS,
                             limit=5) for user in USERS.split(",")]
        for tweet in chain(*tweets):
            # Pre-process the tweet before checking for filter words!
            if ((not redis_conn.exists(f"tweets:{tweet.id_}")) and
                is_viewable_tweet(
                    lemmatize(remove_stopwords(tweet.tweet)))):
                _tweet = {
                    f"tweet:{tweet.id_}": {
                        "id": tweet.id_,
                        "tweet": tweet.tweet,
                        "user_name": tweet.user_name,
                        "date": tweet.date_,
                        "likes": tweet.likes,
                        "link": tweet.link,
                        "replies": tweet.replies,
                        "retweets": tweet.retweets}}
                with redis_conn.pipeline() as pipe:
                    for tweet_id, content in _tweet.items():
                        pipe.hmset(tweet_id, content)
                    pipe.execute()
                    redis_conn.bgsave()
                redis_conn.expire(f"tweets:{tweet.id_}",
                                  timedelta(days=2))
        print("Done storing tweets!")
        time.sleep(10000)
