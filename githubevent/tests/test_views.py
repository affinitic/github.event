import unittest
from pyramid.httpexceptions import HTTPNotFound
from pyramid import testing
from git.event.event import PullRequestEvent
from githubevent.testing import DummyGitHubPullRequest, DummyGitHubRequest


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_unknown_event_type(self):
        from githubevent.views import githubevent
        request = DummyGitHubRequest()
        request.event = None
        with self.assertRaises(HTTPNotFound):
            githubevent(request)

    def test_known_event_type(self):
        from githubevent.views import githubevent
        request = DummyGitHubPullRequest()
        info = githubevent(request)
        self.assertEqual(info, {})

    def test_view_subscriber(self):
        L = self.config.testing_add_subscriber(PullRequestEvent)
        self.assertEqual(len(L), 0)
        request = DummyGitHubPullRequest()
        request.registry = self.config.registry
        from githubevent.views import githubevent
        githubevent(request)
        self.assertEqual(len(L), 1)
