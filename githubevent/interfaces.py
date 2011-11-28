# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from zope.interface import Interface, Attribute


class GitHubRequest(Interface):
    request = Attribute('The request object')


class IPullRequest(GitHubRequest):
    """
    An event type that is a Pull request
    """

class IPush(GitHubRequest):
    """
    An event type that is a Push
    """
