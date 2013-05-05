###############################################
# Ryan Shea & Charles Jhin
# CSE 30332 Programming Paradigms
# Final Project

import cherrypy 
import os.path
import fnmatch
from scripts import page_include


#get ip address of this machine and print it for debugging purposes
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
print(s.getsockname()[0])
s.close()

###############################################
# Main Page
class homepage:
  def __init__(self):
    self.signin = signin_auth()

  def index(self):
	#check if valid cookie authentication.  If valid run normal, if not run signin page
    cookie = cherrypy.request.cookie
    for name in cookie:
      if (name=='user'):
		#add get_script functions and do HTML head. Also create header. 
		HTML = page_include.get_script()+'''
		  <head>
			<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css" rel="stylesheet">
			<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>		 
		  </head>

		  <body style="background-image:url(http://win-8.de/wp-content/uploads/2011/03/windows-8-m3-wallpaper1.jpg)">
			<div class="row-fluid" style="text-align:left; padding-left:30px;">
			  <h1><font color="#E0E0E0">swag</font></h1>
			</div>
		'''       
    		#HTML Body
		#Loop through modules, call each using get_script 
		mod_count = 0
		for module in module_names:
			HTML += '<div class="span4" style="background-color:#FFF; padding:0 10px 10px 10px; margin-bottom:5px; border-radius:1em; opacity:0.65; filter:alpha(opacity=65)">' #module
			HTML += '<h3 style="text-align:right; margin:0 0 -5px 0">'+module+'</h3>' #title
			HTML += '<script>HttpRequest("'+module+'")</script></div>'       #body
			mod_count += 1              
		HTML = HTML + '</body>'
		return HTML

    #at this point no cookie was found so print out authentication
    HTML= '''
	  <form class="form-signin" action="signin">
        <h2 class="form-signin-heading">Please sign in</h2>
        <input name="info" type="text" class="input-block-level" placeholder="Username">
        <input name="info" type="password" class="input-block-level" placeholder="Password">
        <button class="btn btn-large btn-primary" type="submit">Sign in</button>
      </form>'''
    return HTML
  index.exposed = True

#signin page authentication stuff
class signin_auth:
	def index(self, info=None):
		if(info[0]=='admin' and info[1]=='password'):
			cookie_input = cherrypy.response.cookie
			cookie_input['user'] = 'yes'
			cookie_input['user']['path'] = '/'

		raise cherrypy.HTTPRedirect("../../")

	index.exposed = True 
###############################################
# Import and Initialize all "modules" 
#
#   Ex:
#   root.'url' = 'package_name'.'module_class_name'()

# Import the list of desired modules from modules/modules.txt
module_names = []
for filename in os.listdir('./modules'):
      if fnmatch.fnmatch(filename, '*.py') and filename not in('__init__.py'):
        filename = filename[:-3]
        module_names.append(filename)

root = homepage()

# Initialize all modules
for module in module_names:
	import_command = 'from modules import '+module
	exec import_command
	code = 'root.'+module+' = '+module+'.module_'+module+'()'
	exec code

###############################################
# Let's get this party started
if __name__ == '__main__':

	conf = {
		'global': {
			'server.socket_host': '0.0.0.0',
			'server.socket_port': 8001},
		'/': {
			'tools.staticdir.root': os.path.join(os.path.abspath(__file__))[:-13]},
		'/images': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': 'images/'}
	}

#	cherrypy.quickstart(root, config = os.path.join(os.path.dirname(__file__), 'conf.conf'))
	cherrypy.quickstart(root, '/', config = conf)
