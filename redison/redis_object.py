import redis
import pickle
from gnutools.utils import id_generator
import time

class RedisObject:
    def __init__(self, data=None,id=None, host="127.0.0.1", port="6379", db=0):
        self._host = host
        self._port = port
        self._db = db
        self._id = id if id is not None else "x" + id_generator(16)
        self._redis = redis.Redis(host=host, port=port, db=db)
        self.set(data) if data is not None else None

    def load_binary(self, binary):
        """
        Nested loading of the json files

        :param binary:
        :return:
        """
        if type(binary)==dict:
            return dict([(k, self.load_binary(v)) for k, v in binary])
        elif type(binary)==bytes:
            return pickle.loads(binary)

    def get(self, blocking=False):
        """
        Pull the redis object from the database

        :return:
        """
        redis_object = self._redis.get(self._id)
        while blocking:
            try:
                assert redis_object is not None
                blocking=False
            except AssertionError:
                time.sleep(0.001)
                redis_object = self._redis.get(self._id)
        return self.load_binary(redis_object)

    def set(self, data):
        """
        Push the redis object to the database

        :param data:
        :return:
        """
        return self._redis.set(self._id, pickle.dumps(data))

    def delete(self):
        """
        Delete the redis object from the database

        :return:
        """
        return self._redis.delete(self._id)
