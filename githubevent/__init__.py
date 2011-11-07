from pyramid.config import Configurator
from githubevent.resources import Root


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.scan('.views')
    return config.make_wsgi_app()
