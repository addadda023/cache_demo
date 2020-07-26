import itertools
import random
from scripts.user import User
from scripts.redis_conn import redis
from scripts.user_graph import return_degree
import logging
import pickle

# log transport
logging.basicConfig(config=logging.DEBUG)


def create_user_graph():
    user_names = [''.join(_) for _ in list(itertools.permutations('abcde'))]
    locations = [''.join(_) for _ in list(itertools.permutations('uvwxy'))]

    # create user
    users = [User(name=user_name, location=location) for user_name, location in zip(user_names, locations)]
    # randomly assign each user 5 friends
    for user in users:
        random_friends = random.sample(users, k=10)
        for random_friend in random_friends:
            if random_friend != user:
                user.friends.add(random_friend)

    return users


def push_user_graph(users, r: redis.get_redis()):
    # get degrees
    for user in users:
        # get random user
        other = random.sample(users, k=1)[0]
        logging.info('User: {}, friend: {}'.format(user.name, other.name))
        # find degree of connection
        degree = return_degree(user, other)
        logging.info('Degree of connection: {}'.format(str(degree)))

        # push to redis
        d = {user: [other,degree]}
        pickled_object = pickle.dumps(d)
        r.set(user.name, pickled_object)
        logging.info('Pushed user graph to redis.')
