# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from zope.interface import implements
from .interfaces import IPullRequest


class GitHubRequest(object):

    def __init__(self, request):
        self.request = request


class PullRequest(GitHubRequest):
    """
    A pull request
    """
    implements(IPullRequest)
