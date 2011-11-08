from pyramid.config import Configurator
from githubevent.resources import Root
from githubevent.request import gitHubRequestFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    includeme(config)
    return config.make_wsgi_app()


def includeme(config):
    config.set_request_factory(gitHubRequestFactory)
    config.scan('.views')
