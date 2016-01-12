import os

import webapp2
from google.appengine.ext.webapp import template


def render_template(handler, template_name, template_values):
    path = os.path.join(os.path.dirname(__file__), '..', 'templates', template_name)

    print('\n' * 10)
    print(path)

    html = template.render(path, template_values)
    handler.response.out.write(html)


class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'index.html', {})
