from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory(
        'spencersgeruchallenge')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('random', '/quotes/random')
    config.add_route('quote_by_num', '/quotes/{quoteNum}')

    config.scan()
    return config.make_wsgi_app()