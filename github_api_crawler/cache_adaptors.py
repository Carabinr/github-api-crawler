from abc import ABC, abstractmethod
from .exceptions import GithubCacheAdapterException
import redis


class AbstractCacheAdapter(ABC):

    cache = None
    @abstractmethod
    def getval(self, key:str):
        pass

    @abstractmethod
    def setval(self, key:str, val:str):
        pass


class RedisCacheAdapter(AbstractCacheAdapter):

    def __init__(self, url:str=None):
        if not url:
            raise GithubCacheAdapterException('URL Is required. '
                                              'See: https://redis.readthedocs.io/en/stable/examples/connection_examples.html')

        self.cache = redis.from_url(url)

    def getval(self, key:str):
        return self.cache.get(key)

    def setval(self, key:str, val:str) -> None:
        self.cache.set(key, val)


class MemoryCacheAdapter(AbstractCacheAdapter):
    def __init__(self):
        self.cache = {}

    def getval(self, key:str):
        return self.cache.get(key)

    def setval(self, key:str, val:str) -> None:
        self.cache[key] = val
