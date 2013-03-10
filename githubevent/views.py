from git.event.event import PushEvent, PullRequestEvent
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


@view_config(renderer='string')
def githubevent(request):
    notify = request.registry.notify
    if request.event == 'pull_request':
        notify(PullRequestEvent(request))
        return {}
    if request.event == 'push':
        notify(PushEvent(request))
        return {}
    raise HTTPNotFound()
