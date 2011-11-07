# -*- coding: utf-8 -*-
from optparse import OptionParser


def getOptions():
    parser = OptionParser()
    parser.add_option("-u", "--user", dest="user",
                      help="user needed to connect", metavar="USER")
    parser.add_option("-p", "--password", dest="password",
                      help="password needed to connect", metavar="PASSWORD")
    parser.add_option("-U", "--repouser", dest="repouser",
                      help="user where the repository stands", metavar="REPOUSER")
    parser.add_option("-r", "--repo", dest="repo",
                      help="user where the repository stands", metavar="REPO")
    parser.add_option("-o", "--urltonotify", dest="url",
                      help="url to notify with new pull request", metavar="URL")
    (options, args) = parser.parse_args()
    if options.user is None or\
            options.password is None or\
            options.repouser is None or\
            options.repo is None or\
            options.url is None:
        parser.error("wrong number of arguments")
    return options


def main():
    options = getOptions()
    from github import github
    gh = github.GitHub(options.user, options.password)
    gh.repos.createHook(options.repouser, options.repo, 'web',
            config=dict(url=options.url, content_type='json'),
            events=['pull_request', 'push'])
    print gh.repos.listHooks(options.repouser, options.repo)

if __name__ == '__main__':
    main()
