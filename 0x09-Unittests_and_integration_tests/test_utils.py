#!/usr/bin/env python3
""" unittesting Module """

from typing import Mapping, Sequence
import unittest
from unittest.case import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ access_nested_map unit testing class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, res):
        """ access_nested_map result testing method """
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence):
        """ access_nested_map exceptions testing method """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ get_json unit testing class """

    @parameterized.expand([
        ("http://example.com", {"test_payload": True}),
        ("http://holberton.io", {"test_payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ get_json result and number of calls testing method """
        with patch('requests.get') as patched:
            patched.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            patched.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ memoize decorator unit testing class """

    def test_memoize(self):
        """ memoize decorator result and number of calls testing method """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, patched.return_value)
            self.assertEqual(test_class.a_property, patched.return_value)
            patched.assert_called_once()
