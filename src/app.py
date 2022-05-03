#import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

#Functions
def index_page(req):
   return FileResponse("index.html")
def product_page(req):
   return FileResponse("productInfo.html")
def kvp_page(req):
   return FileResponse("kvp.html")
def about_us_page(req):
   return FileResponse("aboutUs.html")
def project_page(req):
   return FileResponse("project.html")

#Line below tells executor to start from here
if __name__ == '__main__':
   with Configurator() as config:
 
      # Create a route called home
      config.add_route('home', '/')
      # Bind the view (defined by index_page) to the route named ‘home’
      config.add_view(index_page, route_name='home')

      # Adds different routes possible in the website
      config.add_route('product', '/productInfo')
      # Directs the route to the function that can generate the view
      config.add_view(product_page, route_name='product')

      # Adds different routes possible in the website
      config.add_route('kvp', '/kvp')
      # Directs the route to the function that can generate the view
      config.add_view(kvp_page, route_name='kvp')

      # Adds different routes possible in the website
      config.add_route('about_us', '/about_us')
      # Directs the route to the function that can generate the view
      config.add_view(about_us_page, route_name='about_us')

      # Adds different routes possible in the website
      config.add_route('project', '/project')
      # Directs the route to the function that can generate the view
      config.add_view(project_page, route_name='project')

    #    # Create a route that handles server HTTP requests at: /photos/photo_id
    #    config.add_route('photos', '/photos/{photo_id}')
       
       # Add a static view
       # This command maps the folder “./public” to the URL “/”
       # So when a user requests geisel-1.jpg as img_src, the server knows to look
       # for it in: “public/geisel-1.jpg”
      config.add_static_view(name='/', path='./public', cache_max_age=3600)

       # Create an app with the configuration specified above
      app = config.make_wsgi_app()
   server = make_server('0.0.0.0', 6000, app) # Start the application on port 6543
   server.serve_forever()