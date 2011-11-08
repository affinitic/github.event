# -*- coding: utf-8 -*-
"""
github.evetn

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from pyramid.testing import DummyRequest
from githubevent.request import BaseGitHubRequest, BaseGitHubPullRequest


class DummyGitHubRequest(DummyRequest, BaseGitHubRequest):

    def __init__(self, params=None, environ=None, headers=None, path='/',
                 cookies=None, post=None, **kw):
        DummyRequest.__init__(self, params, environ, headers, path,
                 cookies, post, **kw)
        self.headers['Content-Type'] = 'application/json'


class DummyGitHubPullRequest(BaseGitHubPullRequest, DummyGitHubRequest):
    pass
