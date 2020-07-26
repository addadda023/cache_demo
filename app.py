from scripts.redis_conn import redis
from flask import Flask


app = Flask(__name__)
redis.init_app(app)


