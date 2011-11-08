# -*- coding: utf-8 -*-
import unittest
from pyramid import testing
from githubevent.request import gitHubRequestFactory, GitHubRequest, GitHubPullRequest


class RequestFactoryTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def testPullRequestEvent(self):
        EVENT_ID = 'pull_request'
        request = gitHubRequestFactory({'X-Github-Event': EVENT_ID})
        self.assertEqual(request.__class__, GitHubPullRequest)
        self.assertEqual(request.event, EVENT_ID)

    def testUnknownGitHubEvent(self):
        request = gitHubRequestFactory({'X-Github-Event': 'foo'})
        self.assertEqual(request.__class__, GitHubRequest)
        self.assertEqual(request.event, None)

    def testEmptyGitHubEvent(self):
        request = gitHubRequestFactory({})
        self.assertEqual(request.__class__, GitHubRequest)
        self.assertEqual(request.event, None)
