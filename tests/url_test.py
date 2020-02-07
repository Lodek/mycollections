#!/usr/bin/env python
"""

"""
from unittest import TestCase, main
from url import URL

class URLTest(TestCase):

    def setUp(self):
        self.url = URL()

    def test_truediv_appends_path(self):
        """
        Given URL object with resource_path not empty
        When I use the / operator on URL
        Then the returned URL should have the updated resource_path
        """
        self.url.resouce_path = ['usr']
        url = self.url / 'bin'
        self.assertEqual(url.resource_path,
                         ['usr', 'bin'])

    def test_truediv_pops_path(self):
        """
        Given URL object with resource_path not empty
        When I execture url / '..'
        Then the element of resource_path should not exist in the return
        """
        self.url.resource_path = 'usr bin'.split()
        url = self.url / '..'
        self.assertEqual(url.resource_path, ['usr'])

    def test_truediv_popping_on_empty_path(self):
        """
        Given URL object iwth resource_path empty
        When I call url / '..'
        Then exception should not be raised
        Then returned object resource path should be empty
        """
        self.url.resource_path = []
        url = self.url / '..'
        self.assertEqual(url.resource_path, [])

if __name__ == '__main__':
    main()
