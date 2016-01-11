import os
import webapp2

from google.appengine.ext.webapp import template
from controllers import main_page_controller

app = webapp2.WSGIApplication([
    ('/', main_page_controller.MainPage),
], debug=True)
