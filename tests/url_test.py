#!/usr/bin/env python
"""

"""
from unittest import TestCase, main
from mycollections.url import URL

class URLTest(TestCase):

    def setUp(self):
        self.url = URL()

    def test_truediv_appends_path(self):
        """
        Given URL object with resource_path not empty
        When I use the / operator on URL
        Then the returned URL should have the updated resource_path
        """
        self.url.resource_path = ['usr']
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
        Given URL object with resource_path empty
        When I call url / '..'
        Then exception should not be raised
        Then returned object resource path should be empty
        """
        self.url.resource_path = []
        url = self.url / '..'
        self.assertEqual(url.resource_path, [])

    def test_mul_inserting_domain(self):
        """
        Given URL object with domain name
        When I insert a domain to the domains list
        Then returned url should have all domains
        """
        self.url.full_domain = 'google com'.split()
        url = self.url * 'books'
        self.assertEqual(url.full_domain,
                         'books google com'.split())

    def test_mul_removing_with_domains(self):
        """
        Given URL object with domains
        When I multiply '..' (parent)
        Then returned object should have one less domain
        """
        self.url.full_domain = 'google com'.split()
        url = self.url * '..'
        self.assertEqual(url.full_domain,
                         ['com'])

    def test_mul_removing_without_domains(self):
        """
        Given URL with empty domain list
        When I mutiply '..' on the empty list
        Then returned object should have no domain
        Then no exception should be raised
        """
        self.url.full_domain = []
        url = self.url * '..'
        self.assertEquals(url.full_domain,
                          [])



if __name__ == '__main__':
    main()
