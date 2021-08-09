from dataclasses import dataclass
from typing import List

import twint


@dataclass
class Tweet:
    """DS for storing Tweets for further processing"""
    id_: int
    tweet: str
    link: str
    user_name: str
    date_: str
    likes: int
    replies: int
    retweets: int


def get_tweets(user_name: str, search_term: str,
               limit: int = 20) -> List[Tweet]:
    """Fetch LIMIT number of tweets from a particular USER_NAME"""
    c = twint.Config()
    c.Limit = limit
    c.Username = user_name
    c.Pandas = True
    c.Output = "none"
    c.Search = search_term
    twint.run.Search(c)
    _tweets = twint.storage.panda.Tweets_df

    tweets = []
    for id_, tweet, date_, link, likes, replies, retweets in zip(
            _tweets['id'],
            _tweets['tweet'],
            _tweets['date'],
            _tweets['link'],
            _tweets['nlikes'],
            _tweets['nreplies'],
            _tweets['nretweets']):
        tweets.append(Tweet(id_=id_, tweet=tweet,
                            link=link,
                            user_name=user_name,
                            date_=date_, likes=likes,
                            replies=replies,
                            retweets=retweets))
    return tweets
