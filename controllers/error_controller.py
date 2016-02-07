import os
import webapp2
from google.appengine.ext.webapp import template
from utilities import template

class ErrorPage(webapp2.RequestHandler):
    def get(self):
        template.render_template(self, 'error.html', {})
