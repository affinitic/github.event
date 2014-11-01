# -*- coding: utf-8 -*-
import github
from github.Hook import Hook
from github.Repository import Repository


def get_github_api():
    from netrc import netrc
    login, account, password = netrc().authenticators('github.com')
    return github.Github(login, password)


def repr_hook(self):
    return '<github.Hook.Hook id=%s object name=%s config=%s events=%s>' % (
        self.id,
        self.name,
        self.config,
        self.events)

Hook.__repr__ = repr_hook


def repr_repo(self):
    return '<github.Repository.Repository name=%s' % (self.name)

Repository.__repr__ = repr_repo
