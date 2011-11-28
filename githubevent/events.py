# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from zope.interface import implements
from .interfaces import IPullRequest
from .interfaces import IPush


class GitHubRequest(object):

    def __init__(self, request):
        self.request = request


class PullRequest(GitHubRequest):
    """
    A pull request
    """
    implements(IPullRequest)


class Push(GitHubRequest):
    """
    A github push
    """
    implements(IPush)