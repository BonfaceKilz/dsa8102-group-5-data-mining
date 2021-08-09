from better_profanity import profanity
from typing import List

from nltk.tokenize import word_tokenize

import os
import nltk


def remove_stopwords(words: List) -> str:
    """Remove stopwords from WORDS"""
    from nltk.corpus import stopwords
    nltk.download("stopwords")  # Only run once!
    stop_words = set(stopwords.words("english"))
    return " ".join(
        [word for word in words if word.casefold() not in stop_words])


def stem(text: str) -> str:
    """Reduce words to their roots"""
    from nltk.stem import PorterStemmer
    words = word_tokenize(text)
    stemmer = PorterStemmer()
    return " ".join([stemmer.stem(word) for word in words])


def lemmatize(words: List) -> str:
    """Reduce words to their core meaning"""
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet')  # Only run once
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word) for word in words])


def is_viewable_tweet(tweet: str) -> bool:
    """Use `better_profanity` to filter out profane and political words"""
    WORDLIST = os.path.join(
        os.path.dirname(__file__),
        "political_words.txt"
    )
    profanity.load_censor_words_from_file(WORDLIST)
    return profanity.contains_profanity(tweet)
