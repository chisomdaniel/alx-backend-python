#!/usr/bin/env python3
'''Parameterize a unit test'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch
from unittest.mock import Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    '''the test class for access_nested_map function'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''check that it outputs the correct output'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Parameterize a unit test'''
        with self.assertRaises(KeyError,
                               msg="KeyError: '{}'".format(path[-1])):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Mock HTTP calls test'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_request):
        '''test get json'''
        mock = Mock()
        mock.json.return_value = test_payload
        mock_request.return_value = mock
        print('Value', get_json(test_url))
        self.assertEqual(get_json(test_url), test_payload)
