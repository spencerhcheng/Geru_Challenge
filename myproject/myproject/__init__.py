from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from .models import DBSession, Base
from sqlalchemy import engine_from_config
from pyramid.renderers import JSONP

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # Engine configuration #
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    my_session_factory = SignedCookieSessionFactory(
        'spencersgeruchallenge')
    config = Configurator(settings=settings, session_factory=my_session_factory, root_factory='.models.Root')
    config.include('pyramid_jinja2')
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_renderer('jsonp', JSONP(param_name='callback'))

    # Endpoint routes
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('random', '/quotes/random')
    config.add_route('test_db', '/test_db')
    config.add_route('quote_by_num', '/quotes/{quoteNum}')
    config.add_route('query', '/api_query')

    config.scan()
    return config.make_wsgi_app()
