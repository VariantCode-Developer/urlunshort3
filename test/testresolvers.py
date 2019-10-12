import unittest

from urlunshort3 import resolve_short

# all of these should resolve to https://github.com/remotephone/urlunshort3


class TestResolve(unittest.TestCase):
    def test_generic(self):
        urls = ["https://bit.ly/2nBRa1c"]
        for url in urls:
            dst = resolve_short(url)
            self.assertEqual(dst, "https://github.com/remotephone/urlunshort3")

    def test_404(self):
        assert resolve_short("http://example.org/adsfasd.fasdfasads,masdf") == None

    def test_bad_host(self):
        assert resolve_short("http://alewklfafadsfaewfadasfa/foo") == None


if __name__ == "__main__":
    unittest.main()
