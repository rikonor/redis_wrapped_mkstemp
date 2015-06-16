import uuid

def redis_wrapped_mkstemp(redis, namespace="tmp"):
    """
    :param redis: A redis.StrictRedis client handle
    :type redis: redis.StrictRedis
    :param namespace: A prefix for the file name
    :type namespace: str

    The purpose of this wrapper is to create a unique blob name in redis
    Return a file path to use

    User is responsible for cleaning the filename from Redis
    """
    while True:
        # Generate random filename
        fpath = "/tmp/" + namespace + str(uuid.uuid4())

        # Use this file path as a unique id and if this value is unique in redis then return it for further use
        if redis.setnx('blob:{}'.format(fpath), '') is True:
            # Create the file (same as touch)
            open(fpath, 'w').close()
            return fpath
