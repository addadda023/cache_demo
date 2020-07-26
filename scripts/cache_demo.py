from scripts.redis_conn import redis
import logging
from scripts.populate_user_graph import *

# log transport
logging.basicConfig(level=logging.INFO)

# redis
r = redis.get_redis()
# create user graph and push to redis
users = create_user_graph()
# push to redis
push_user_graph(users, r)
