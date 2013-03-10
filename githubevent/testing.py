# -*- coding: utf-8 -*-
"""
github.evetn

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from pyramid.testing import DummyRequest
from .request import GitHubPullRequest


class DummyGitHubRequest(DummyRequest):

    def __init__(self, params=None, environ=None, headers=None, path='/',
                 cookies=None, post=None, **kw):
        self.environ = {}
        self.headers = {}
        self.headers['Content-Type'] = 'application/json'


class DummyGitHubPullRequest(DummyGitHubRequest, GitHubPullRequest):
    pass
