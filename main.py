import webapp2
from controllers import main_page_controller
from controllers import about_controller
from controllers import contact_controller
from controllers import error_controller
from controllers import gallery_controller
from controllers import shows_controller

# sends us to the appropriate controller for the URL
app = webapp2.WSGIApplication([
    ('/', main_page_controller.MainPage),
    ('/about', about_controller.AboutPage),
    ('/contact', contact_controller.ContactPage),
    ('/error', error_controller.ErrorPage),
    ('/gallery', gallery_controller.GalleryPage),
    ('/shows', shows_controller.ShowsPage)
], debug=True)
