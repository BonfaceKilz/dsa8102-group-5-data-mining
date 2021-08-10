import redis

from flask import Blueprint
from flask import render_template

general = Blueprint("general", __name__)


@general.route("/")
def upload_metadata_with_no_token():
    redis_conn = redis.Redis(decode_responses=True)
    return render_template(
        "index.html",
        tweets=[redis_conn.hgetall(tweet)
                for tweet in redis_conn.keys("tweet*")])
