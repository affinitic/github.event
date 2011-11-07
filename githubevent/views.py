from .events import PullRequest
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


@view_config(renderer='string')
def githubevent(request):
    event_type = request.headers.get('X-Github-Event')
    notify = request.registry.notify
    if event_type == 'pull_request':
        notify(PullRequest(request))
        return {}
    raise HTTPNotFound()
