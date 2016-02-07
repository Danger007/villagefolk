import webapp2

from controllers import main_page_controller

app = webapp2.WSGIApplication([
    ('/', main_page_controller.MainPage),
    #('/', main_page_controller.MainPage),
    #('/', main_page_controller.MainPage),
    #('/', main_page_controller.MainPage),
    #('/', main_page_controller.MainPage),
], debug=True)
