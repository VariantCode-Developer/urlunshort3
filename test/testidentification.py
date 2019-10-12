import unittest
from urlunshort3 import is_shortened, define_services


class TestResolve(unittest.TestCase):
    def test_is_shortened(self):
        services = define_services()
        for service in services:
            print(service)
            assert is_shortened(
                "http://{}/asdf".format(service)
            ), "http://{}/asdf".format(service)
            assert not is_shortened("http://{}".format(service)), "http://{}".format(
                service
            )


if __name__ == "__main__":
    unittest.main()
