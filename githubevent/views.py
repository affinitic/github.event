from .events import PullRequest
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


@view_config(renderer='string')
def githubevent(request):
    notify = request.registry.notify
    if request.event == 'pull_request':
        notify(PullRequest(request))
        return {}
    raise HTTPNotFound()
