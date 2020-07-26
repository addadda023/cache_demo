from unittest import TestCase
from scripts.redis_conn import redis
from scripts.user import User
from scripts.user_graph import return_degree
import itertools
import random


class TestRedisConn(TestCase):
    def test_ping(self):
        r = redis.get_redis()
        response = r.ping()
        self.assertEqual(response, True)

    def test_cache_user_degree(self):
        user_names = [''.join(_) for _ in list(itertools.permutations('abcde'))]
        locations = [''.join(_) for _ in list(itertools.permutations('vwxyz'))]

        # create user
        users = [User(name=user_name, location=location) for user_name, location in zip(user_names, locations)]
        # randomly assign each user 5 friends



