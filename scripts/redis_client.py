import redis
import logging

# log transport
logging.basicConfig(level=logging.DEBUG)


class Redis:
    def __init__(self):
        self.app = None
        self.driver = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        host = '127.0.0.1'
        port = 7001
        try:
            self.driver = redis.Redis(host=host, port=port)
            logging.info('Successfully connected to redis at {}'.format(str(host)))
            return self.driver
        except redis.exceptions.ConnectionError as redis_con_error:
            logging.error(redis_con_error)

    def get_redis(self):
        if not self.driver:
            return self.connect()
        return self.driver
