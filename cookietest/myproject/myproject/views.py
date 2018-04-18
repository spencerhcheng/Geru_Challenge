from pyramid.view import (view_config, view_defaults)
import requests
import random
from myproject.quotes import quotes as q
from .models import DBSession, Page, json_serial, without_keys
import uuid
import transaction
import json
import datetime
from pyramid.response import Response

def session_id(session, path):
    """
    Generate random UUID if doesn't exist
    """
    visit = session
    if 'id' not in session:
        visit['id'] = str(uuid.uuid4())

    DBSession.add(Page(session_identifier=visit['id'], page=path))
    transaction.commit()

    return visit

@view_defaults(renderer='templates/mytemplate.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @property
    def counter(self):
        """
        Counts sessions
        """
        session = self.request.session
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1
        return session['counter'] 

    @view_config(route_name='test_db', renderer='templates/testDB_view.pt')
    def DB_view(self):
        pages = DBSession.query(Page)
        return dict(pages=pages)

    @view_config(route_name='home')
    def my_view(request):
        """
        Home view. http://localhost:8080
        """
        web_display = "Web Challenge 1.0"
        return {
            'web_display':web_display,
            'project': 'myproject'}

    @view_config(route_name='quotes')
    def quotes(self):
        """
        Displays all quotes. http://localhost:8080/quotes
        """
        session = session_id(self.request.session, self.request.current_route_url()) 
        quotes = q.get_quotes()
        return {
            'quotes': quotes,
            'project': 'myproject'}

    @view_config(route_name='quote_by_num')
    def quote_by_num(self):
        """
        Displays quote denoted by number. http://localhost:8080/quotes/<quote_number>
        """
        quote_number = self.request.matchdict['quoteNum']
        quote = q.get_quote(quote_number)
        session = session_id(self.request.session, self.request.current_route_url()) 
        return {
            'quote': quote,
            'project': 'myproject'}


    @view_config(route_name='random')
    def random(self):
        """
        Displays a random quote. http://localhost:8080/quotes/random
        """
        randNum = random.randint(0, 18)
        random_quote = q.get_quote(str(randNum))
        session = session_id(self.request.session, self.request.current_route_url()) 
        return {
            'random_quote': random_quote,
            'project': 'myproject'}

#def datetime_handler(pdate):
#    if isinstance(pdate, datetime.datetime):
#        return pdate.isoformat()

@view_config(route_name='query', renderer='jsonp')
def consultas(request):
    db_query = DBSession.query(Page).all()
    query_list = ([ob.__dict__ for ob in db_query])
    result = []
    for dictionary in query_list:
        result.append(without_keys(dictionary, {"_sa_instance_state", "uid"}))
    json_string = json.dumps([ob for ob in result], default=json_serial)
    return Response(json=json.loads(json_string))

