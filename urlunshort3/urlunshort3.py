import logging
from urllib.parse import urlparse, urlsplit
from .resolvers import generic_resolver

"""
.. attribute:: services

List of domains of known URL shortening services.
"""


def define_services():
    services = [
        "bit.ly",
        "t.co"
        # "1url.com",
        # "adcraft.co",
        # "adcrun.ch",
        # "adf.ly",
        # "adflav.com",
        # "aka.gr",
        # "bee4.biz",
        # "bit.do",
        # "bit.ly",
        # "bitly.com",
        # "budurl.com",
        # "buzurl.com",
        # "cektkp.com",
        # "cli.gs",
        # "crisco.com",
        # "cutt.us",
        # "dft.ba",
        # "fa.by",
        # "filoops.info",
        # "fun.ly",
        # "fzy.co",
        # "gog.li",
        # "golinks.co",
        # "goo.gl",
        # "hit.my",
        # "id.tl",
        # "is.gd",
        # "ity.im",
        # "j.mp",
        # "lemde.fr",
        # "linkto.im",
        # "lnk.co",
        # "longurl.org",
        # "lurl.no",
        # "moourl.com",
        # "nov.io",
        # "ow.ly",
        # "p6l.org",
        # "picz.us",
        # "prettylinkpro.com",
        # "q.gs",
        # "qr.net",
        # "scrnch.me",
        # "shortquik.com",
        # "sk.gy",
        # "smallr.com",
        # "snipr.com",
        # "snipurl.com",
        # "snurl.com",
        # "su.pr",
        # "t.co",
        # "tiny.cc",
        # "tinyurl.com",
        # "tota2.com",
        # "tr.im",
        # "tweez.me",
        # "twitthis.com",
        # "u.bb",
        # "u.to",
        # "v.gd",
        # "viralurl.biz",
        # "viralurl.com",
        # "virl.ws",
        # "vur.me",
        # "vzturl.com",
        # "x.co",
        # "xlinkz.info",
        # "xtu.me",
        # "yourls.org",
        # "yu2.it",
        # "zpag.es"
    ]
    return services


def resolve_short(url, timeout=None):
    """
    Resolve shortened URL to a target URL. If the URL could not be resolved,
    return None.

    :argument url: the url to resolve

    :argumet timeout: the max tix to wait for the URL to resolve in seconds
        There's currently no way of telling if a request failed due to
        a timeout or because the URL could not be resolved!

    :returns: the resolved URL. None if URL could not be resolved

    """
    # services = define_services()
    # for service in services:
    #     if service not in url:
    #         logging.error("[!] - {} is not supported")
    #         raise Exception

    result = generic_resolver(url)
    return result


def is_shortened(url):
    """Check if the url appears to be shortened, based on the services
    whitelist. **Note:** This will be a best-effort thing, as the list
    if services has to be kept up to date. Also note that valid URLs on
    shortening services (like bit.ly/apidocs) will be assumed to be a
    shortened url.

    :argument url: The URL to check

    :returns: true or false
    """
    parts = urlsplit(url)
    if not parts.scheme and not parts.hostname:
        # couldn't parse anything sensible, try again with a scheme.
        parts = urlsplit("http://" + url)
        # yes, I dknow about the default_scheme argument to ursplit,
        # and no, it doesn't actully work.
    services = define_services()
    print(services)
    return bool(parts.hostname in services and parts.path)
