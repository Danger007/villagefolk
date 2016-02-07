import os
import webapp2
from google.appengine.ext.webapp import template
from utilities import template


##def render_template(handler, template_name, template_values):
#    path = os.path.join(os.path.dirname(__file__), '..', 'templates', template_name)

#    html = template.render(path, template_values)
#    handler.response.out.write(html)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template.render_template(self, 'index.html', {})
