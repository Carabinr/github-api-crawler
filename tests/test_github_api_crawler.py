import os
import unittest
import responses
from github_api_crawler.api import Github
from github_api_crawler.exceptions import GithubException


class TestGithub_api_crawler(unittest.TestCase):


    def setUp(self):
        self.crawler = Github('fake123')


    def tearDown(self):
        pass

    def test_api_key_required(self):

        with self.assertRaises(GithubException):
            api = Github()

    def test_missing_user(self):
        pass

    @responses.activate
    def test_update_stats_with_502(self):
        rsp1 = responses.Response(
            method='GET',
            url='https://api.github.com/orgs/learn-co-students/repos',
            status=502,
            json={}
        )
        responses.add(rsp1)

        with self.assertRaises(GithubException):
            r = self.crawler.get_org_repositories('learn-co-students')

