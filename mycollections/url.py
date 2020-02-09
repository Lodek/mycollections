import re

class InvalidUrlErro(RuntimeError):
    def __init__(self, *args, **kwargs):
        super(*args, **kwargs)

class URL:
    """
    High level URL manipulation akin to pathlib's Path object.
    URL objects are immutable and methods are fluent.
    """
    URL_formatter = '{}://{}/{}'
    QUERY_SEPARATOR = '&'
    QUERY_ASSIGNMENT = '='

    def __init__(self):
        self.scheme = ''
        self.full_domain = []
        self.resource_path = []
        self.port = 0

    def parse_url(self, url):
        """

        """
        parse_resource_path(url)
        parse_domain(url)
        parse_scheme(url)

    def parse_handler(f):
        """Decorator to abstract error handling in the parse functions"""
        def parse_wrapper(self, url):
            try:
                f(self, url)
            except IndexError:
                error_msg = f'Invalid url {url}, error parsing {f.__name__}'
                raise InvalidUrlError(error_msg)
        return parse_wrapper


    @parse_handler
    def parse_domain(self, url):
        """
        Receive URL and extract the full domain from it, store the result
        in the full_domain list.
        The top level domain is stored at the end of the list and sub domains
        are inserted at the beginning.
        """
        #little monster
        domain_re = re.compile(r'(?<=:\/\/)((\w+)($|((\.\w+)?(?=\/|.)))*)')
        match = domain_re.search(url)
        self.full_domain = match[0].split('.')

    @parse_handler
    def parse_resource_path(self, url):
        resource_path_re = re.compile(r'(?<!:\/\/)(?<=\/)((\w+)(\/\w+(?=\/|$))*)')
        match = resource_path_re.search(url)
        self.resource_path = match[0].split('/')

    @parse_handler
    def parse_scheme(self, url):
        scheme_re = re.compile(r'^(\w+):\/\/')
        match = scheme_re.search(url)
        self.scheme = match[0]


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
        

    def __str__(self):
        resource_path = '/'.join(self.resource_path)
        full_domain = '.'.join(self.full_domain)
        return self.URL_formatter.format(self.scheme, full_domain, resource_path)

    
    def query(self, query, query_join='?'):
        """Receive dictionary with key-values of an URL query.
        Return string of the current URL with the query string
        query_join defines the symbol that will be use to concatenate the url
        with the query string, defaults to ?"""
        format_query = lambda query : self.stringfy_dict(query, self.QUERY_ASSIGMENT, self.QUERY_SEPARATOR)
        return self.get_url(paths) + query_join + format_query(query)


    @staticmethod
    def stringfy_dict(d, kv_join, separator):
        return separator.join([str(key) + kv_join + str(value) for key, value in d.items()])

