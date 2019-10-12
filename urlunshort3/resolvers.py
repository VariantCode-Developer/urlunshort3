"""
This module contains resolvers for url shorteners. A resolver takes a netloc
(host[:port] and path) and returns a URL as a string.
"""
import logging
import requests
from functools import wraps


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
def generic_resolver(url, timeout=None):
    """
    Generic url fetcher that assumes the target service will response sanely
    to a HEAD request for the url.

    returns the full url or None if the url could not be resolved.
    """
    request_error = range(400, 600)

    if timeout:
        r = requests.head(url, timeout=timeout)
    else:
        r = requests.head(url)
    redirect_codes = [300, 301, 302, 307, 308]
    if r.status_code in redirect_codes:
        logging.debug(
            '"{}" returned a {} status code'.format(url, r.status_code)
        )  # will not print anything
        return r.headers["Location"]  # None by default
    elif r.status_code in request_error:
        logging.error(
            '"{}" returned a {} response'.format(url, r.status_code)
        )  # will print a message to the console
    else:
        logging.debug('URL "{}" returned an unhandled response'.format(url))
        raise Exception

    return None
