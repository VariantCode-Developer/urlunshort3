from urlunshort3 import resolve_short

# all of these should resolve to http://bitbucket.org/runeh/urlunshort/
urls = (
    "http://bit.ly/qlKaI",
    "http://budurl.com/qlsh",
    "http://cli.gs/5XqsgT",
    "http://fa.by/59cb97",
    "http://is.gd/ZRQo",
    "http://lurl.no/gQ",
    "http://moourl.com/p8r43",
    "http://smallr.com/9ki",
    "http://snipr.com/jzcj6",
    "http://snipurl.com/jzcj6",
    "http://snurl.com/jzcj6",
    "http://su.pr/17SSKk",
    "http://tiny.cc/yTOuU",
    "http://tr.im/ohoC"
)

def test_generic():
    for url in urls:
        dst = resolve_short(url)
        assert dst=="http://bitbucket.org/runeh/urlunshort/", "got %s  from %s" % (dst, url)


def test_404():
    assert resolve_short("http://example.org/adsfasd.fasdfasads,masdf") == None

def test_bad_host():
    assert resolve_short("http://alewklfafadsfaewfadasfa/foo") == None

