import re


class URL:
    """
    High level URL manipulation akin to pathlib's Path object.
    URL objects are immutable and methods are fluent.
    """
    URL_formatter = '{}://{}/{}'
    QUERY_SEPARATOR = '&'

    def __init__(self):
        self.scheme = ''
        self.full_domain = []
        self.resource_path = []
        self.port = 0

    def parse_url(self):
        """

        """
        url_matcher = re.compile(r'^(.*)://(.*?(?:/)?)((?<=/).*)')
        domain_name_matcher = re.compile(r'^(.*)/')
        self.paths = paths
        try:
            scheme_match = scheme_re.search(url)
            domain_match = domain_name_re.search(scheme_match.groups(2))
            self.scheme = scheme_match.groups(1)
            self.domain_name = domain_match.groups(1)
        except AttributeError as e:
            print('invalid url')

    def parse_domain(self, domain_str):
        self.full_domain = domain_str.split('.')

    def parse_resource_path(self, resource_str):
        self.resource_path = resource_str.split('/')

    def parse_scheme(self, scheme):
        pass


    def __truediv__(self, other):
        """Concatenate other as part of the resource path, Return a new URL.
        Notes:
        - `other` should be value str()-able.
        - The string '..' is a special value and removes the last element of the path.
        """
        resource_path = [p for p in self.resource_path]
        if str(other) == '..':
            try:
                resource_path.pop()
            except IndexError:
                pass
        else:
            resource_path.append(str(other))
        url = URL.from_params(scheme=self.scheme, full_domain=self.full_domain,
                              resource_path=resource_path)
        return url


    def __mul__(self, other):
        """Insert `other` as the first element in the domain name, return a new URL.
        Notes:
        - `Other` should be value str()-able.
        - The string '..' is a special value and removes the last element of the domain.
        """
        #Refactor this, recycled logic from above
        full_domain = [p for p in self.full_domain]
        if str(other) == '..':
            try:
                full_domain.pop(0)
            except IndexError:
                pass
        else:
            full_domain.insert(0, str(other))
        url = URL.from_params(scheme=self.scheme, full_domain=full_domain,
                              resource_path=self.resource_path)
        return url


    @classmethod
    def from_params(cls, scheme, full_domain, resource_path):
        url = cls()
        url.scheme = scheme
        url.full_domain = full_domain
        url.resource_path = resource_path
        return url


    @classmethod
    def oneshot(cls, url, paths):
        """Return a formatted url from a base url and the desired paths."""
        builder = cls(url)
        return builder.get(paths)
        

    def get_url(self, paths):
        """Build url from a list of paths"""
        paths = self.paths + paths
        joined_paths = '/'.join(paths)
        return self.URL_formatter.format(self.scheme, self.domain_name, joined_paths)


    def add_query(self, paths, query):
        format_query = lambda query : stringfy_dict(query, '=', self.QUERY_SEPARATOR)
        query_join = '?'
        return self.get_url(paths) + query_join + format_query(query)


    @staticmethod
    def stringfy_dict(d, kv_join, separator):
        return separator.join([str(key) + kv_join + str(value) for key, value in d.items()])

