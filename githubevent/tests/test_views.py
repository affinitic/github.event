import unittest
from pyramid.httpexceptions import HTTPNotFound
from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_unknown_event_type(self):
        from githubevent.views import githubevent
        request = testing.DummyRequest(headers={'Content-Type': 'application/json'})
        with self.assertRaises(HTTPNotFound):
            githubevent(request)

    def test_known_event_type(self):
        from githubevent.views import githubevent
        request = testing.DummyRequest(headers={'X-Github-Event': 'pull_request',
                                                'Content-Type': 'application/json'})
        info = githubevent(request)
        self.assertEqual(info, {})
