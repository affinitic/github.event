# -*- coding: utf-8 -*-
import unittest
from pyramid import testing
from git.event.request import GitRequest
from githubevent.request import gitHubRequestFactory, GitHubPullRequest


class RequestFactoryTests(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def testPullRequestEvent(self):
        EVENT_ID = 'pull_request'
        request = gitHubRequestFactory({'HTTP_X_GITHUB_EVENT': EVENT_ID})
        self.assertEqual(request.__class__, GitHubPullRequest)
        self.assertEqual(request.event, EVENT_ID)

    def testUnknownGitHubEvent(self):
        request = gitHubRequestFactory({'HTTP_X_GITHUB_EVENT': 'foo'})
        self.assertEqual(request.__class__, GitRequest)
        self.assertEqual(request.event, None)

    def testEmptyGitHubEvent(self):
        request = gitHubRequestFactory({})
        self.assertEqual(request, None)
