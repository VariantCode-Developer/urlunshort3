from urlunshort3 import services, is_shortened

def test_is_shortened():
    for service in services:
        assert is_shortened("http://%s/asdf" % service), "http://%s/asdf" % service 
        assert not is_shortened("http://%s" % service), "http://%s" % service
