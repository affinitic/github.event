# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
import json
from pyramid.decorator import reify
from pyramid.request import Request


class BaseGitHubRequest(object):
    event = None

    @reify
    def json_body(self):
        return json.loads(self.body, encoding=self.charset)


class GitHubRequest(Request, BaseGitHubRequest):
    pass


class BaseGitHubPullRequest(object):
    event = 'pull_request'

    @property
    def base_repo_url(self):
        return self.json_body['pull_request']['base']['repo']['git_url']

    @property
    def base_repo_name(self):
        return self.json_body['pull_request']['base']['repo']['name']

    @property
    def head_repo_url(self):
        return self.json_body['pull_request']['head']['repo']['git_url']

    @property
    def head_repo_name(self):
        return self.json_body['pull_request']['head']['repo']['name']


class GitHubPullRequest(Request, BaseGitHubPullRequest):
    pass


REQUESTS = {'pull_request': GitHubPullRequest}


def gitHubRequestFactory(env):
    event = env.get('X-Github-Event')
    requestClass = REQUESTS.get(event, GitHubRequest)
    return requestClass(env)
