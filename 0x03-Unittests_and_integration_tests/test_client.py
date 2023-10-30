#!/usr/bin/env python3
'''test client test file'''
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch
from unittest.mock import Mock
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    '''test class'''

    @parameterized.expand([
        ("google", {"key", "value"}),
        ("abc", {"key", "value"})
    ])
    @patch("utils.get_json")
    def test_org(self, org_name, expected, mock_func):
        '''test function'''
        mock_func.return_value = expected
        url = "https://api.github.com/orgs/{}".format(org_name)
        GithubOrgClient(org_name).org

        #mock_func.assert_called_once_with(url)
