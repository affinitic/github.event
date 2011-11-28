from .events import PullRequest
from .events import Push
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


@view_config(renderer='string')
def githubevent(request):
    notify = request.registry.notify
    if request.event == 'pull_request':
        notify(PullRequest(request))
        return {}
    if request.event == 'push':
        notify(Push(request))
        return {}
    raise HTTPNotFound()
