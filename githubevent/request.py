# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from git.event.request import GitPullRequest, GitPushRequest


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

    @property
    def base_repo_url(self):
        return self.json_body['repository']['html_url']

    @property
    def base_repo_name(self):
        return self.json_body['repository']['name']

    @property
    def commits(self):
        return [GitHubCommit(commit_body) for commit_body in self.json_body['commits']]

    @property
    def author(self):
        return self.json_body['pusher']['name']

    @property
    def author_email(self):
        return self.json_body['pusher']['email']


class GitHubCommit(object):

    def __init__(self, commit_body):
        self.commit_body = commit_body

    @property
    def id(self):
        return self.commit_body['id']

    @property
    def branch(self):
        # XXX tester commit dans autre branch
        return "master"

    @property
    def username(self):
        return self.commit_body['author']['username']

    @property
    def message(self):
        return self.commit_body['message']

    @property
    def timestamp(self):
        return self.commit_body['timestamp']

    @property
    def url(self):
        return self.commit_body['url']
