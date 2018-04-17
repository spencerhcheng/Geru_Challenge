
from pyramid.view import (view_config, view_defaults)
import requests
import random
from myproject import quotes as q

@view_defaults(renderer='templates/mytemplate.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    @property
    def counter(self):
        session = self.request.session
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1
        return session['counter'] 

    # Home view. http://localhost:8080
    @view_config(route_name='home')
    def my_view(request):
        web_display = "Web Challenge 1.0"
        return {
            'web_display':web_display,
            'project': 'myproject'}

    # Displays all quotes. http://localhost:8080/quotes
    @view_config(route_name='quotes')
    def quotes(self):
               
        quotes = q.get_quotes()
        return {
            'quotes': quotes,
            'project': 'myproject'}

    # Displays quote denoted by number. http://localhost:8080/quotes/<quote_number>
    @view_config(route_name='quote_by_num')
    def quote_by_num(self):
        quote_number = self.request.matchdict['quoteNum']
        quote = q.get_quote(quote_number)
        return {
            'quote': quote,
            'project': 'myproject'}


    # Displays a random quote. http://localhost:8080/quotes/random
    @view_config(route_name='random')
    def random(self):
        randNum = random.randint(0, 18)
        random_quote = q.get_quote(str(randNum))
        return {
            'random_quote': random_quote,
            'project': 'myproject'}
