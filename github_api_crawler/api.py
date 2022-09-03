import time
import requests
from typing import Dict, List, Union
from loguru import logger
from requests.exceptions import JSONDecodeError
from .exceptions import GithubException
from .cache_adaptors import AbstractCacheAdapter, MemoryCacheAdapter


class Github(object):

    BEARER_TOKEN = ""
    BASE_URL = 'https://api.github.com'
    HEADERS = {}

    def __init__(self, bearer_token: str = None, cache: AbstractCacheAdapter = None) -> None:

        if not cache:
            self.cache = MemoryCacheAdapter()

        if not bearer_token:
            raise GithubException('Bearer Token is required')

        self.BEARER_TOKEN = bearer_token

        self.HEADERS = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {self.BEARER_TOKEN}"
        }

    def _epoch_to_human(self, future_time:int) -> str:
        """
        Convert a UNIX epoch into a human-readable format.
        eg - {days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s) remain.
        or, "No time remaining" if the time is in the past

        Args:
            future_time (int): A UNIX epoch represented as an integer

        Returns:
            String telling time remaining in human-readable format
        """
        current_time = int(time.time())  # current epoch time
        time_left = int(future_time) - current_time  # returns seconds
        days = time_left // 86400
        hours = time_left // 3600 % 24
        minutes = time_left // 60 % 60
        seconds = time_left % 60

        if time_left <= 0:
            return "No time remaining"
        else:
            return f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s) remain."

    def _update_stats(self, r:requests.Response):
        """

        Args:
            r:

        Returns:

        """
        rate_limits = [
            'X-RateLimit-Limit',
            'X-RateLimit-Remaining',
            'X-RateLimit-Used',
            'X-RateLimit-Resource',
            'X-RateLimit-Reset',
        ]

        self.cache.setval('time-left', self._epoch_to_human(r.headers['X-RateLimit-Reset']))

        for _ in rate_limits:
            self.cache.setval(_, r.headers[_])

    def _get(self, target:str) -> Union[List[Dict], Dict]:
        """


        Args:
            target (str): The target URL fragment that is appended to the base url.

        Returns:
            A JSON response from Github. It is either a List or a Dict.
        Raises:
            GithubException
        """
        r = requests.get(f"{self.BASE_URL}/{target}", headers=self.HEADERS)

        self._update_stats(r)

        if not r.ok:
            error = r.json()
            error['status_code'] = r.status_code
            error['url'] = r.url
            raise GithubException(error)

        return r.json()

    def get_org(self, org:str) -> Dict:
        return self._get(f"orgs/{org}")

    def get_repo(self, full_name:str) -> Dict:
        return self._get(f"repos/{full_name}")

    def get_repo_contributors(self, full_name:str) -> List[Dict]:
        """
        Get all public contributors to the repo. In a weird twist
        Args:
            full_name (str): the owner/name path of the repo (eg simplecto/boom)

        Returns:
            Empty list or List of Dict
        """
        try:
            output = self._get(f"repos/{full_name}/contributors")
        except JSONDecodeError:
            logger.debug(f"Got empty response in {full_name} that caused JSONDecodeError exception.")
            output = []

        return output

    def get_org_public_members(self, org:str) -> List[Dict]:
        return self._get(f"orgs/{org}/public_members")

    def get_org_repositories(self, org:str) -> List[Dict]:
        return self._get(f"orgs/{org}/repos")

    def get_user_owned_repositories(self, username:str) -> List[Dict]:
        """
        List all repositories owned by the user.

        NOTE: This defaults to the repos where user is OWNER.

        Args:
            username: Github username

        Returns:
            List of results List of Dict
        """
        return self._get(f"users/{username}/repos")

    def get_public_orgs_for_user(self, username:str) -> List[Dict]:
        return self._get(f"users/{username}/orgs")

    def get_user(self, username:str) -> Dict:
        return self._get(f"users/{username}")
