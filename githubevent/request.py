# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
import json
from pyramid.decorator import reify
from git.event.request import GitPullRequest, GitPushRequest, GitRequest


class GitHubPullRequest(GitPullRequest):

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


class GitHubPushRequest(GitPushRequest):

    @reify
    def json_body(self):
        return json.loads(self.POST.get('payload'))


REQUESTS = {'pull_request': GitHubPullRequest,
            'push': GitHubPushRequest}


def gitHubRequestFactory(env):
    event = env.get('HTTP_X_GITHUB_EVENT')
    if event:
        requestClass = REQUESTS.get(event, GitRequest)
        return requestClass(env)
