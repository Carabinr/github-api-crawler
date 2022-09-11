import unittest
from github_api_crawler.cache_adaptors import RedisCacheAdapter
from github_api_crawler.exceptions import GithubCacheAdapterException
import os
import uuid

class TestGithub_redis_cache_adapters(unittest.TestCase):

    def setUp(self):
        self.adapter = RedisCacheAdapter(url=os.getenv('CACHE_URL'))

    def tearDown(self):
        pass

    def test_successful_write(self):
        key = uuid.uuid4().hex
        message = "yourmomgoestocollege"
        self.adapter.setval(key, message)

        again = self.adapter.getval(key)
        self.assertEqual(again, message)

    def test_exception_thrown(self):
        with self.assertRaises(GithubCacheAdapterException):
            r = RedisCacheAdapter()
