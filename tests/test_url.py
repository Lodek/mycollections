#!/usr/bin/env python
"""

"""
from unittest import TestCase, main
from mycollections.url import URL

class URLTest(TestCase):
    """
    Test suite for URL class
    """
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
        self.assertEqual(url.full_domain,
                          [])

    def test_url_parsing_no_resource_no_trailing_slash(self):
        """
        Given an url without resource path and without a trailing slash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://google.com')
        self.assertEqual(url.full_domain, ['google', 'com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, [])


    def test_url_parsing_no_resource_trailing_slash(self):
        """
        Given an url without resource path and a trailing resource dash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://google.com/')
        self.assertEqual(url.full_domain, ['google', 'com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, [])

    def test_url_parsing_resource_no_trailing_slash(self):
        """
        Given an url with a resource path and without a trailing slash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://google.com/yeezy')
        self.assertEqual(url.full_domain, ['google', 'com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, ['yeezy'])


    def test_url_parsing_resource_no_trailing_slash(self):
        """
        Given an url with a resource path and without a trailing slash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://google.com/yeezy/')
        self.assertEqual(url.full_domain, ['google', 'com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, ['yeezy'])


    def test_url_parsing_resources_no_trailing_slash(self):
        """
        Given an url with a resource path and without a trailing slash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://google.com/yeezy/yeet')
        self.assertEqual(url.full_domain, ['google', 'com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, ['yeezy', 'yeet'])

    def test_url_parsing_resources_trailing_slash(self):
        """
        Given an url with a resource path and with a trailing slash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://google.com/yeezy/yeet/')
        self.assertEqual(url.full_domain, ['google', 'com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, ['yeezy', 'yeet'])

    def test_url_parsing_domain_and_resources_trailing_slash(self):
        """
        Given an url with a resource path and with a trailing slash
        When I build an URL object
        Then the url should be parsed correctly
        """
        url = URL.from_string('http://com/yeezy/yeet/')
        self.assertEqual(url.full_domain, ['com'])
        self.assertEqual(url.scheme, 'http')
        self.assertEqual(url.resource_path, ['yeezy', 'yeet'])

    def test_url_parsing_with_one_query(self):
        """
        Given an url with one query parameter
        When parsed
        Then url object query should be correct
        """
        url = URL.from_string('http://google.com/ok?key1=value1')
        self.assertEqual(url.query, {'key1':'value1'})
        
    def test_url_parsing_with_two_queries(self):
        """
        Given an url with two query parameters
        When parsed
        Then url object query should be correct
        """
        url = URL.from_string('http://google.com/ok?key1=value1&key2=value2')
        self.assertEqual(url.query, {'key1':'value1', 'key2' : 'value2'})

    def test_url_parsing_with_three_queries(self):
        """
        Given an url with three query parameters
        When parsed
        Then url object query should be correct
        """

        url = URL.from_string('http://google.com/ok?key1=value1&key2=value2&key3=value3')
        self.assertEqual(url.query,
                         {'key1':'value1', 'key2':'value2', 'key3':'value3'})


if __name__ == '__main__':
    main()
