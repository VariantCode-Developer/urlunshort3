"""
This module contains resolvers for url shorteners. A resolver takes a netloc
(host[:port] and path) and returns a URL as a string.
"""

import requests 
from functools import wraps

# Currently there is only a single, generic resolver, which should(tm) work
# with all services. One could add more resolvers here, so as to be more
# polite with the url shortening services that provides APIs for developers
# There are probably also some services with a landing page for ads etc, which
# one needs to handle differently

def _io_error_handling(fun):
    """
    Catch connection errors for requests
    """

    @wraps(fun)
    def wrapped(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except requests.ConnectionError:
            return None
    return wrapped


@_io_error_handling
def generic_resolver(netloc, path, timeout=None):
    """
    Generic url fetcher that assumes the target service will response sanely
    to a HEAD request for the url.

    returns the full url or None if the url could not be resolved.
    """
    if timeout:
        response = requests.head(netloc, timeout=timeout)
    else:
        response = requests.head(netloc)
    redirect_codes = [300, 301, 302, 307, 308]
    if response.status in redirect_codes:
        return response.headers("Location") # None by default
    return None