# -*- coding: utf-8 -*-
import argh
from .utils import get_github_api


@argh.arg('repouser', help='user where the repository stands')
@argh.arg('repo', help='name of the repository (optional)', default=None)
def listHooks(repouser, repo, gh=None):
    if gh is None:
        gh = get_github_api()
    if repo is None:
        org = gh.get_organization(repouser)
        repos = org.get_repos()
    else:
        repos = [gh.get_repo("%s/%s" % (repouser, repo))]
    for repo in repos:
        for hook in repo.get_hooks():
            if hook.active:
                yield repo, hook


def main():
    parser = argh.ArghParser()
    argh.set_default_command(parser, listHooks)
    parser.dispatch()

if __name__ == '__main__':
    main()
